// Publication data will be injected by Jekyll
let publicationsData = [];
let searchIndex = null;

// Generate BibTeX for a publication
function generateBibtex(pub) {
  const key = pub.openalex_id || 'pub' + Math.random().toString(36).substr(2, 9);
  const authors = pub.authors ? pub.authors.replace(/, et al\./g, ' and others').replace(/, /g, ' and ') : '';
  const type = pub.type === 'article' ? 'article' : 'misc';

  return `@${type}{${key},
  title = {${pub.title || ''}},
  author = {${authors}},
  journal = {${pub.journal || ''}},
  year = {${pub.year || ''}},
  doi = {${pub.doi || ''}}
}`;
}

// Copy BibTeX to clipboard
function copyBibtex(index) {
  if (publicationsData[index]) {
    const bibtex = generateBibtex(publicationsData[index]);
    navigator.clipboard.writeText(bibtex).then(() => {
      const btn = document.querySelector(`[data-bibtex-index="${index}"]`);
      if (btn) {
        const original = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => { btn.textContent = original; }, 1500);
      }
    });
  }
}

// Download all BibTeX
function downloadAllBibtex() {
  const allBibtex = publicationsData.map(generateBibtex).join('\n\n');
  const blob = new Blob([allBibtex], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'publications.bib';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// Toggle abstract visibility
function toggleAbstract(index) {
  const abstract = document.querySelector(`[data-abstract-index="${index}"]`);
  const btn = document.querySelector(`[data-abstract-btn="${index}"]`);
  if (abstract && btn) {
    const isHidden = abstract.style.display === 'none' || !abstract.style.display;
    abstract.style.display = isHidden ? 'block' : 'none';
    btn.textContent = isHidden ? 'Hide Abstract' : 'Show Abstract';
  }
}

// Dark Mode Toggle
function toggleDarkMode() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);

  // Update button text
  const themeIcons = document.querySelectorAll('.theme-icon');
  themeIcons.forEach(icon => {
    icon.innerHTML = newTheme === 'dark' ? '&#9788;' : '&#9790;';
  });

  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.innerHTML = newTheme === 'dark'
      ? '<span class="theme-icon">&#9788;</span> Light Mode'
      : '<span class="theme-icon">&#9790;</span> Dark Mode';
  }
}

// Initialize theme from localStorage
function initTheme() {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    if (savedTheme === 'dark') {
      const themeToggle = document.querySelector('.theme-toggle');
      if (themeToggle) {
        themeToggle.innerHTML = '<span class="theme-icon">&#9788;</span> Light Mode';
      }
    }
  }
}

// Mobile Menu Toggle
function toggleMobileMenu() {
  const sidebar = document.getElementById('sidebarNav');
  const toggleBtn = document.querySelector('.mobile-menu-toggle');

  if (sidebar && toggleBtn) {
    sidebar.classList.toggle('mobile-active');
    toggleBtn.classList.toggle('active');
  }
}

// Close mobile menu when clicking a link
function initMobileMenuClose() {
  const sidebarLinks = document.querySelectorAll('.sidebar-nav a');
  sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
      const sidebar = document.getElementById('sidebarNav');
      const toggleBtn = document.querySelector('.mobile-menu-toggle');
      if (sidebar && toggleBtn && window.innerWidth < 1024) {
        sidebar.classList.remove('mobile-active');
        toggleBtn.classList.remove('active');
      }
    });
  });
}

// Back to Top Button
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTop');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });
  }
}

// Publication Filters - WARNING-18 fix: dynamic year filter based on visible publications
function initPublicationFilters() {
  const yearSelect = document.getElementById('yearFilter');
  if (!yearSelect) return;

  // Wait for publicationsData if not ready
  if (!publicationsData || !publicationsData.length) {
    setTimeout(initPublicationFilters, 200);
    return;
  }

  // Populate year filter with count of publications per year
  const yearCounts = {};
  publicationsData.forEach(p => {
    if (p.year) {
      yearCounts[p.year] = (yearCounts[p.year] || 0) + 1;
    }
  });

  const years = Object.keys(yearCounts).sort((a, b) => b - a);
  years.forEach(year => {
    const option = document.createElement('option');
    option.value = year;
    option.textContent = `${year} (${yearCounts[year]})`;
    yearSelect.appendChild(option);
  });
}

function filterPublications() {
  const yearFilter = document.getElementById('yearFilter')?.value || 'all';
  const topicFilter = document.getElementById('topicFilter')?.value || 'all';
  const accessFilter = document.getElementById('accessFilter')?.value || 'all';

  const pubItems = document.querySelectorAll('.pub-item');
  let visibleCount = 0;

  pubItems.forEach(item => {
    const year = item.dataset.year;
    const title = item.dataset.title || '';
    const abstract = item.dataset.abstract || '';
    const searchText = (title + ' ' + abstract).toLowerCase();
    const isOpen = item.dataset.open === 'true';

    let show = true;

    // Year filter
    if (yearFilter !== 'all' && year !== yearFilter) {
      show = false;
    }

    // Topic filter - search in title AND abstract for better matching
    if (topicFilter !== 'all') {
      const topicKeywords = {
        'credit': ['credit', 'risk', 'default', 'loan', 'lending', 'borrower'],
        'network': ['network', 'graph', 'centrality', 'topology', 'node', 'edge'],
        'machine': ['machine learning', 'deep learning', 'neural', 'ai', 'artificial', 'algorithm', 'model'],
        'p2p': ['p2p', 'peer-to-peer', 'lending', 'platform', 'crowdfunding'],
        'crypto': ['crypto', 'bitcoin', 'blockchain', 'digital asset', 'cryptocurrency', 'defi']
      };
      const keywords = topicKeywords[topicFilter] || [];
      if (!keywords.some(kw => searchText.includes(kw))) {
        show = false;
      }
    }

    // Access filter
    if (accessFilter === 'open' && !isOpen) {
      show = false;
    }

    item.classList.toggle('hidden', !show);
    if (show) visibleCount++;
  });

  // Show/hide no results message
  let noResultsEl = document.getElementById('noFilterResults');
  if (visibleCount === 0) {
    if (!noResultsEl) {
      noResultsEl = document.createElement('div');
      noResultsEl.id = 'noFilterResults';
      noResultsEl.className = 'pub-item';
      noResultsEl.style.textAlign = 'center';
      noResultsEl.style.color = 'var(--text-light)';
      noResultsEl.innerHTML = '<em>No publications match the selected filters. Try adjusting your criteria.</em>';
      document.getElementById('publicationList')?.appendChild(noResultsEl);
    }
    noResultsEl.style.display = 'block';
  } else if (noResultsEl) {
    noResultsEl.style.display = 'none';
  }

  // Update citation metrics for visible publications (WARNING-17 fix)
  updateFilteredCitationMetrics();
}

function resetFilters() {
  const yearFilter = document.getElementById('yearFilter');
  const topicFilter = document.getElementById('topicFilter');
  const accessFilter = document.getElementById('accessFilter');

  if (yearFilter) yearFilter.value = 'all';
  if (topicFilter) topicFilter.value = 'all';
  if (accessFilter) accessFilter.value = 'all';

  filterPublications();
}

// Citation Metrics - CRITICAL-04 fix: ensure proper initialization
function updateCitationMetrics() {
  // Wait for publicationsData to be available
  if (!publicationsData || !publicationsData.length) {
    // Retry after a short delay if data not ready
    setTimeout(updateCitationMetrics, 200);
    return;
  }

  const totalCitations = publicationsData.reduce((sum, p) => sum + (parseInt(p.citations) || 0), 0);
  const avgCitations = publicationsData.length > 0 ? (totalCitations / publicationsData.length).toFixed(1) : '0';
  const openAccessCount = publicationsData.filter(p => p.open_access === true || p.open_access === 'true').length;

  // Update stats banner
  const totalCitationsEl = document.querySelector('#totalCitations .stat-number');
  if (totalCitationsEl) {
    totalCitationsEl.textContent = totalCitations.toLocaleString();
  }

  // Update metric cards
  const metricTotalCitations = document.getElementById('metricTotalCitations');
  const metricAvgCitations = document.getElementById('metricAvgCitations');
  const metricOpenAccess = document.getElementById('metricOpenAccess');

  if (metricTotalCitations) metricTotalCitations.textContent = totalCitations.toLocaleString();
  if (metricAvgCitations) metricAvgCitations.textContent = avgCitations;
  if (metricOpenAccess) metricOpenAccess.textContent = openAccessCount;
}

// WARNING-17 fix: Update metrics based on currently visible publications
function updateFilteredCitationMetrics() {
  if (!publicationsData || !publicationsData.length) return;

  const visibleItems = document.querySelectorAll('.pub-item:not(.hidden):not(#noFilterResults)');
  const visibleIndices = new Set();

  visibleItems.forEach(item => {
    // Get index from the data attributes on bibtex button
    const bibtexBtn = item.querySelector('[data-bibtex-index]');
    if (bibtexBtn) {
      visibleIndices.add(parseInt(bibtexBtn.dataset.bibtexIndex));
    }
  });

  let totalCitations = 0;
  let openAccessCount = 0;
  let count = 0;

  publicationsData.forEach((pub, idx) => {
    if (visibleIndices.has(idx)) {
      totalCitations += parseInt(pub.citations) || 0;
      if (pub.open_access === true || pub.open_access === 'true') openAccessCount++;
      count++;
    }
  });

  const avgCitations = count > 0 ? (totalCitations / count).toFixed(1) : '0';

  // Update metric cards with filtered values
  const metricTotalCitations = document.getElementById('metricTotalCitations');
  const metricAvgCitations = document.getElementById('metricAvgCitations');
  const metricOpenAccess = document.getElementById('metricOpenAccess');

  if (metricTotalCitations) metricTotalCitations.textContent = totalCitations.toLocaleString();
  if (metricAvgCitations) metricAvgCitations.textContent = avgCitations;
  if (metricOpenAccess) metricOpenAccess.textContent = openAccessCount;
}

// Search Functionality using Lunr.js - IMPROVE-03: Now uses generated search index
function initSearch() {
  if (typeof lunr === 'undefined') return;

  // Try to fetch pre-generated search index, fallback to inline generation
  fetch('assets/js/search-index.json')
    .then(response => response.ok ? response.json() : Promise.reject('Not found'))
    .then(data => {
      buildSearchIndex(data.sections, data.publications || []);
    })
    .catch(() => {
      // Fallback to inline index if generated file not available
      buildSearchIndexFallback();
    });
}

function buildSearchIndex(sections, publications) {
  const searchData = [];

  // Add sections from generated index
  sections.forEach(s => {
    searchData.push({ ...s, section: s.id });
  });

  // Add publications from generated index
  publications.forEach((pub, idx) => {
    searchData.push({
      id: pub.id || `pub-${idx}`,
      title: pub.title || '',
      content: `${pub.authors || ''} ${pub.journal || ''} ${pub.year || ''} ${pub.abstract || ''}`,
      section: 'publications'
    });
  });

  searchIndex = lunr(function() {
    this.ref('id');
    this.field('title', { boost: 10 });
    this.field('content');

    searchData.forEach(doc => {
      this.add(doc);
    });
  });

  window.searchData = searchData;
}

function buildSearchIndexFallback() {
  const searchData = [];

  // Fallback sections
  const sections = [
    { id: 'home', title: 'Home', content: 'SNSF credit risk models P2P lending network analysis machine learning' },
    { id: 'team', title: 'Team', content: 'Joerg Osterrieder Lennart Baals Branka Hadji Misheva Yiting Liu researchers' },
    { id: 'research', title: 'Research', content: 'P2P lending credit risk network topology machine learning methods objectives' },
    { id: 'publications', title: 'Publications', content: 'papers journals DOI citations OpenAlex academic' },
    { id: 'analytics', title: 'Analytics', content: 'charts graphs timeline publications year' },
    { id: 'resources', title: 'Resources', content: 'datasets code GitHub Bondora LendingClub data' },
    { id: 'news', title: 'News', content: 'updates announcements latest' },
    { id: 'events', title: 'Events', content: 'conferences presentations workshops COST' },
    { id: 'collaborations', title: 'Collaborations', content: 'Columbia Manchester Renmin Sharjah universities partners' },
    { id: 'funding', title: 'Funding', content: 'SNSF grants CHF money ETH Leading House' },
    { id: 'contact', title: 'Contact', content: 'email form Bern Switzerland address' }
  ];

  // Add publications from global publicationsData
  if (typeof publicationsData !== 'undefined') {
    publicationsData.forEach((pub, idx) => {
      searchData.push({
        id: `pub-${idx}`,
        title: pub.title || '',
        content: `${pub.authors || ''} ${pub.journal || ''} ${pub.year || ''} ${pub.abstract || ''}`,
        section: 'publications'
      });
    });
  }

  sections.forEach(s => searchData.push({ ...s, section: s.id }));

  searchIndex = lunr(function() {
    this.ref('id');
    this.field('title', { boost: 10 });
    this.field('content');

    searchData.forEach(doc => {
      this.add(doc);
    });
  });

  window.searchData = searchData;
}

function performSearch(query) {
  const resultsContainer = document.getElementById('searchResults');
  if (!resultsContainer || !searchIndex || !query.trim()) {
    if (resultsContainer) resultsContainer.innerHTML = '';
    return;
  }

  try {
    const results = searchIndex.search(query + '*');

    if (results.length === 0) {
      resultsContainer.innerHTML = '<div class="search-result-item">No results found</div>';
      return;
    }

    const html = results.slice(0, 5).map(result => {
      const item = window.searchData.find(d => d.id === result.ref);
      if (!item) return '';

      const href = item.id.startsWith('pub-') ? '#publications' : `#${item.id}`;
      const sectionLabel = item.section.charAt(0).toUpperCase() + item.section.slice(1);

      return `
        <a href="${href}" class="search-result-item" onclick="closeSidebarOnMobile()">
          <div class="result-title">${item.title}</div>
          <div class="result-section">${sectionLabel}</div>
        </a>
      `;
    }).join('');

    resultsContainer.innerHTML = html;
  } catch (e) {
    resultsContainer.innerHTML = '';
  }
}

function closeSidebarOnMobile() {
  if (window.innerWidth < 1024) {
    const sidebar = document.getElementById('sidebarNav');
    const toggleBtn = document.querySelector('.mobile-menu-toggle');
    if (sidebar) sidebar.classList.remove('mobile-active');
    if (toggleBtn) toggleBtn.classList.remove('active');
  }
}

// Smooth scroll for navigation links
document.addEventListener('DOMContentLoaded', function() {
  // Initialize theme
  initTheme();

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Highlight active navigation on scroll (both top nav and sidebar)
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-menu a');
  const sidebarLinks = document.querySelectorAll('.sidebar-nav a');

  function highlightNav() {
    let scrollPos = window.scrollY + 100;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        // Highlight top nav
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
        // Highlight sidebar nav
        sidebarLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', highlightNav);
  highlightNav();

  // Add scroll shadow to nav
  const navContainer = document.querySelector('.nav-container');
  if (navContainer) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        navContainer.classList.add('scrolled');
      } else {
        navContainer.classList.remove('scrolled');
      }
    });
  }

  // Initialize features
  initMobileMenuClose();
  initBackToTop();

  // Wait for publicationsData to be set
  setTimeout(() => {
    initPublicationFilters();
    updateCitationMetrics();
    initSearch();
  }, 100);
});
