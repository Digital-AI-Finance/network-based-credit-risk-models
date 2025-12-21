// Visualizations for research analytics

document.addEventListener('DOMContentLoaded', function() {
  // Only initialize if the elements exist
  if (document.getElementById('pubsChart')) {
    initPublicationsChart();
  }
  if (document.getElementById('networkGraph')) {
    initNetworkGraph();
  }
});

// Publications Chart using Chart.js
function initPublicationsChart() {
  const ctx = document.getElementById('pubsChart');
  if (!ctx || typeof Chart === 'undefined') return;

  // Count publications by year from publicationsData
  const yearCounts = {};
  if (typeof publicationsData !== 'undefined') {
    publicationsData.forEach(pub => {
      if (pub.year) {
        yearCounts[pub.year] = (yearCounts[pub.year] || 0) + 1;
      }
    });
  }

  const years = Object.keys(yearCounts).sort();
  const counts = years.map(y => yearCounts[y]);

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: years,
      datasets: [{
        label: 'Publications',
        data: counts,
        backgroundColor: '#1a365d',
        borderColor: '#0f2942',
        borderWidth: 1,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 5 }
        }
      }
    }
  });
}

// Network Graph using D3.js - WARNING-14 & WARNING-19 fixes
function initNetworkGraph() {
  const container = document.getElementById('networkGraph');
  if (!container || typeof d3 === 'undefined') return;

  const width = container.clientWidth || 300;
  const height = 200;

  // Create SVG
  const svg = d3.select('#networkGraph')
    .append('svg')
    .attr('width', width)
    .attr('height', height);

  // WARNING-19 fix: Compute co-authorship from publications data if available
  let nodes = [];
  let links = [];

  if (typeof publicationsData !== 'undefined' && publicationsData.length > 0) {
    // Build author network from publications
    const authorPubs = {};  // author -> count of publications
    const coauthorships = {};  // "author1|author2" -> count

    publicationsData.forEach(pub => {
      if (!pub.authors) return;
      // Split authors by comma or "and"
      const authors = pub.authors.split(/,\s*(?:and\s*)?|(?:\s+and\s+)/).map(a => a.trim()).filter(a => a && a !== 'et al.');

      authors.forEach(author => {
        authorPubs[author] = (authorPubs[author] || 0) + 1;
      });

      // Count co-authorships
      for (let i = 0; i < authors.length; i++) {
        for (let j = i + 1; j < authors.length; j++) {
          const key = [authors[i], authors[j]].sort().join('|');
          coauthorships[key] = (coauthorships[key] || 0) + 1;
        }
      }
    });

    // Create nodes for top authors (by publication count)
    const sortedAuthors = Object.entries(authorPubs)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10);  // Top 10 authors

    const authorSet = new Set(sortedAuthors.map(a => a[0]));
    const coreTeam = ['Joerg Osterrieder', 'J. Osterrieder', 'Lennart Baals', 'L. Baals',
                      'Branka Hadji Misheva', 'B. Hadji Misheva', 'Yiting Liu', 'Y. Liu'];

    sortedAuthors.forEach(([author, count]) => {
      const initials = author.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
      const isCore = coreTeam.some(name => author.includes(name.split(' ').pop()));
      nodes.push({
        id: author,
        name: author,
        initials: initials,
        group: isCore ? 1 : 2,
        pubCount: count
      });
    });

    // Create links between co-authors
    Object.entries(coauthorships).forEach(([key, count]) => {
      const [a1, a2] = key.split('|');
      if (authorSet.has(a1) && authorSet.has(a2)) {
        links.push({ source: a1, target: a2, value: count });
      }
    });
  }

  // Fallback to hardcoded data if no publications or empty result
  if (nodes.length === 0) {
    nodes = [
      { id: 'JO', name: 'J. Osterrieder', initials: 'JO', group: 1, pubCount: 50 },
      { id: 'LB', name: 'L. Baals', initials: 'LB', group: 1, pubCount: 5 },
      { id: 'BM', name: 'B. Hadji Misheva', initials: 'BM', group: 1, pubCount: 8 },
      { id: 'YL', name: 'Y. Liu', initials: 'YL', group: 1, pubCount: 6 },
      { id: 'SC', name: 'S. Chan', initials: 'SC', group: 2, pubCount: 2 },
      { id: 'YZ', name: 'Y. Zhang', initials: 'YZ', group: 2, pubCount: 2 },
      { id: 'JC', name: 'J. Chu', initials: 'JC', group: 2, pubCount: 2 }
    ];
    links = [
      { source: 'JO', target: 'LB', value: 5 },
      { source: 'JO', target: 'BM', value: 8 },
      { source: 'JO', target: 'YL', value: 6 },
      { source: 'LB', target: 'YL', value: 4 },
      { source: 'LB', target: 'BM', value: 3 },
      { source: 'YL', target: 'BM', value: 4 },
      { source: 'JO', target: 'SC', value: 2 },
      { source: 'JO', target: 'YZ', value: 2 },
      { source: 'JO', target: 'JC', value: 2 }
    ];
  }

  // WARNING-14 fix: Optimized force simulation parameters
  const simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(50))
    .force('charge', d3.forceManyBody().strength(-80))  // Reduced from -100
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(20))   // Reduced from 25
    .alphaDecay(0.03)  // Faster decay for quicker settling
    .alphaMin(0.01);   // Stop earlier

  // Draw links
  const link = svg.append('g')
    .selectAll('line')
    .data(links)
    .join('line')
    .attr('stroke', '#c9a227')
    .attr('stroke-opacity', 0.6)
    .attr('stroke-width', d => Math.sqrt(d.value));

  // Draw nodes
  const node = svg.append('g')
    .selectAll('circle')
    .data(nodes)
    .join('circle')
    .attr('r', d => d.group === 1 ? 12 : 8)
    .attr('fill', d => d.group === 1 ? '#1a365d' : '#718096')
    .attr('stroke', '#c9a227')
    .attr('stroke-width', 2)
    .call(drag(simulation));

  // Add labels - use initials for shorter display
  const label = svg.append('g')
    .selectAll('text')
    .data(nodes)
    .join('text')
    .text(d => d.initials || d.id.slice(0, 2).toUpperCase())
    .attr('font-size', '8px')
    .attr('fill', '#2d3748')
    .attr('text-anchor', 'middle')
    .attr('dy', 20);

  // Add tooltips
  node.append('title').text(d => d.name);

  // Update positions on tick
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);

    label
      .attr('x', d => d.x)
      .attr('y', d => d.y);
  });

  // Drag functions
  function drag(simulation) {
    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }

    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }

    function dragended(event) {
      if (!event.active) simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    }

    return d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended);
  }
}
