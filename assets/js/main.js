// Publication data will be injected by Jekyll
let publicationsData = [];

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

// Smooth scroll for navigation links
document.addEventListener('DOMContentLoaded', function() {
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

  // Highlight active navigation on scroll
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-menu a');

  function highlightNav() {
    let scrollPos = window.scrollY + 100;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
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
});
