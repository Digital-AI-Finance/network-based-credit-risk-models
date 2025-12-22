---
layout: default
title: Network-Based Credit Risk Models in P2P Lending Markets
description: SNSF-funded research project developing advanced credit risk models for Peer-to-Peer lending using network analysis and machine learning. Led by Prof. Dr. Joerg Osterrieder at Bern Business School.
image: /images/Osterrieder.jpg
---

<!-- Schema.org Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ResearchProject",
  "name": "Network-Based Credit Risk Models in P2P Lending Markets",
  "description": "SNSF-funded research project developing advanced credit risk models for Peer-to-Peer lending using network analysis and machine learning.",
  "url": "https://digital-ai-finance.github.io/network-based-credit-risk-models/",
  "funder": {
    "@type": "Organization",
    "name": "Swiss National Science Foundation",
    "url": "https://www.snf.ch"
  },
  "funding": {
    "@type": "MonetaryGrant",
    "identifier": "205487",
    "amount": {
      "@type": "MonetaryAmount",
      "value": 387836,
      "currency": "CHF"
    }
  },
  "member": [
    {
      "@type": "Person",
      "name": "Joerg Osterrieder",
      "jobTitle": "Principal Investigator",
      "affiliation": "Bern University of Applied Sciences"
    },
    {
      "@type": "Person",
      "name": "Lennart John Baals",
      "jobTitle": "Researcher"
    },
    {
      "@type": "Person",
      "name": "Branka Hadji Misheva",
      "jobTitle": "Researcher"
    },
    {
      "@type": "Person",
      "name": "Yiting Liu",
      "jobTitle": "Researcher"
    }
  ],
  "startDate": "2022-10-01",
  "endDate": "2025-08-31"
}
</script>

<!-- Mobile Menu Toggle -->
<button class="mobile-menu-toggle" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu">
  <span class="hamburger-icon"></span>
</button>

<nav class="sidebar-nav" id="sidebarNav">
  <div class="sidebar-header">
    <div class="sidebar-title">SNSF Project</div>
    <div class="sidebar-subtitle">Credit Risk Models</div>
  </div>
  <!-- Search Box -->
  <div class="search-container">
    <input type="text" id="searchInput" placeholder="Search..." onkeyup="performSearch(this.value)">
    <div id="searchResults" class="search-results"></div>
  </div>
  <ul>
    <li><a href="#home">Home</a></li>
    <li><a href="#announcement">Announcement</a></li>
    <li><a href="#team">Team</a></li>
    <li><a href="#research">Research</a></li>
    <li><a href="#phd-publications">PhD Publications</a></li>
    <li><a href="#research-outputs">Research Outputs</a></li>
    <li><a href="#analytics">Analytics</a></li>
    <div class="nav-section">Resources</div>
    <li><a href="#resources">Datasets & Code</a></li>
    <li><a href="#news">News</a></li>
    <li><a href="#events">Events</a></li>
    <div class="nav-section">Network</div>
    <li><a href="#collaborations">Collaborations</a></li>
    <li><a href="#funding">Funding</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#publications">All Pubs</a></li>
    <div class="nav-section">Reports</div>
    <li><a href="{{ site.baseurl }}/final-report/" class="nav-report-link">Final Scientific Report</a></li>
  </ul>
  <!-- Dark Mode Toggle -->
  <div class="theme-toggle-container">
    <button class="theme-toggle" onclick="toggleDarkMode()" aria-label="Toggle dark mode">
      <span class="theme-icon">&#9790;</span> Dark Mode
    </button>
  </div>
</nav>

<nav class="nav-container">
  <ul class="nav-menu">
    <li><a href="#home">Home</a></li>
    <li><a href="#announcement">Announcement</a></li>
    <li><a href="#team">Team</a></li>
    <li><a href="#research">Research</a></li>
    <li><a href="#phd-publications">PhD Pubs</a></li>
    <li><a href="#research-outputs">Outputs</a></li>
    <li><a href="#analytics">Analytics</a></li>
    <li><a href="#resources">Resources</a></li>
    <li><a href="#news">News</a></li>
    <li><a href="#events">Events</a></li>
    <li><a href="#collaborations">Collaborations</a></li>
    <li><a href="#funding">Funding</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="{{ site.baseurl }}/final-report/" class="nav-report-link">Final Report</a></li>
  </ul>
</nav>

<section id="home">

<div class="logo-banner">
  <img src="assets/images/logos/snsf-logo.svg" alt="Swiss National Science Foundation" loading="lazy">
  <img src="assets/images/logos/bfh-logo.svg" alt="Bern University of Applied Sciences" loading="lazy">
  <button onclick="toggleDarkMode()" class="btn-theme" aria-label="Toggle dark mode">&#9790;</button>
  <button onclick="window.print()" class="btn-pdf">Print / Save PDF</button>
</div>

<div class="project-status-badge" style="text-align: center; margin-bottom: 1rem;">
  <span style="background: linear-gradient(135deg, #22c55e, #16a34a); color: white; padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: 600; font-size: 0.9rem;">PROJECT COMPLETED</span>
</div>

<div class="stats-banner">
  <div class="stat-item">
    <span class="stat-number">387,836</span>
    <span class="stat-label">CHF Funding</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">{{ site.data.publications | size }}</span>
    <span class="stat-label">Publications</span>
  </div>
  <div class="stat-item" id="totalCitations">
    <span class="stat-number">--</span>
    <span class="stat-label">Total Citations</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">5</span>
    <span class="stat-label">Collaborations</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">5</span>
    <span class="stat-label">Researchers</span>
  </div>
</div>

> This SNSF-funded project develops advanced, interpretable credit risk models tailored specifically to the needs of Peer-to-Peer (P2P) lending markets using network analysis and machine learning.

</section>

---

<section id="announcement">
<h2>Project Completion Announcement</h2>
<div style="background:#f8f9fa;border-left:4px solid #0a66c2;padding:1rem;font-size:0.85rem;line-height:1.4;">
<p><strong>PROJECT COMPLETED: Network-Based Credit Risk Models in P2P Lending Markets</strong></p>
<p>I am delighted to announce the successful completion of our SNSF-funded research project (Grant 205487) on network-based credit risk models in peer-to-peer lending markets.</p>
<p><strong>What we achieved:</strong> Over three years (Oct 2022 - Aug 2025), we developed novel machine learning methodologies that leverage network topology to assess credit risk in P2P lending. Our supervised network-based approach fundamentally advances how we understand borrower relationships and default prediction.</p>
<p><strong>Key outcomes:</strong> 52+ scientific publications | 23 ORCID-registered publications (2024-2025) in Expert Systems with Applications, Finance Research Letters, Quantitative Finance, Energy Economics | 12 open-access Zenodo deposits | 2 PhD researchers trained | CHF 387,836 total funding</p>
<p><strong>Core team:</strong> <a href="https://www.linkedin.com/in/lennart-john-baals-a621aa193/">@Lennart John Baals</a> | <a href="https://www.linkedin.com/in/yiting-liu-313587266/">@Yiting Liu</a> | <a href="https://www.linkedin.com/in/hadjimisheva/">@Branka Hadji Misheva</a> | @Stefan Lyocsa</p>
<p><strong>International collaborators:</strong> @Ali Hirsa (Columbia) | @Stephen Chan (AUS) | @Jeffrey Chu (Renmin) | @Yuanyuan Zhang (Manchester) | @Blanka Stadler (Masaryk)</p>
<p><strong>Institutions:</strong> <a href="https://www.bfh.ch">@BFH</a> | <a href="https://www.utwente.nl">@University of Twente</a> | <a href="https://www.snf.ch">@SNSF</a> | <a href="https://www.cost.eu">@COST Association</a></p>
<p>Our research demonstrates that network position contains genuine predictive signal for default risk. A key finding: simple degree centrality often matches complex metrics like PageRank, offering practitioners an accessible entry point to network-based credit assessment.</p>
<p><em>#CreditRisk #P2PLending #MachineLearning #NetworkAnalysis #FinTech #OpenScience #SNSF #DigitalFinance #AI #XAI</em></p>
</div>
</section>

---

<section id="team">

<h2>Our Team</h2>

<em>International cooperation between Bern Business School (Switzerland) and partner institutions</em>

<div class="team-grid">
{% for member in site.data.team %}
<div class="team-card" itemscope itemtype="https://schema.org/Person">
  <img src="{{ member.image }}" alt="{{ member.name }}" loading="lazy" itemprop="image">
  <span class="role-badge">{{ member.role }}</span>
  <h4 itemprop="name">{{ member.name }}</h4>
  <p class="institution" itemprop="affiliation">{{ member.institution }}{% if member.institution2 %}<br>{{ member.institution2 }}{% endif %}</p>
  <p class="bio" itemprop="description">{{ member.bio }}</p>
  <div class="profile-links">
    {% if member.orcid and member.orcid != "pending" %}<a href="https://orcid.org/{{ member.orcid }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer" title="ORCID" class="orcid-link external-link"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" alt="ORCID" loading="lazy"> ORCID</a>{% endif %}
    {% if member.google_scholar %}<a href="{{ member.google_scholar }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer" title="Google Scholar" class="external-link">Scholar</a>{% endif %}
    {% if member.linkedin %}<a href="{{ member.linkedin }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer" title="LinkedIn" class="external-link">LinkedIn</a>{% endif %}
    {% if member.website %}<a href="{{ member.website }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer" title="Website" class="external-link">Web</a>{% endif %}
  </div>
</div>
{% endfor %}
</div>

</section>

---

<section id="research">

<h2>Research Project</h2>

<h3>Background</h3>

Peer-to-peer (P2P) lending has become an increasingly popular alternative to traditional bank lending, allowing individuals and businesses to borrow money directly from investors through online platforms without involving banks. While this method offers advantages such as higher returns for investors and greater access to credit for borrowers, it also brings unique risks. The decentralized nature of P2P lending means that loans are funded entirely by investors, without the safeguards of bank intermediation.

<h3>Rationale</h3>

The growing presence of P2P lending markets, especially during economic crises, exposes these platforms to significant risks, including adverse selection and moral hazard. Unlike traditional banks that use long-term relationships and extensive data to evaluate borrowers, P2P platforms have less detailed information and face higher levels of uncertainty. There is a critical need for robust credit risk models that can accurately assess the creditworthiness of borrowers in these markets.

<h3>Objectives</h3>

This project aims to develop <strong>advanced, interpretable credit risk models</strong> tailored specifically to the needs of P2P lending markets. These models will address the unique challenges of P2P lending, such as:

- Higher information asymmetry
- Less regulation compared to traditional banking
- Increased risk during economic downturns

The ultimate goal is to enhance trust between investors and P2P platforms by providing accurate tools for evaluating and mitigating credit risk.

<h3>Methods</h3>

The project develops credit risk models using <strong>network-based approaches</strong>, analyzing the connections between borrowers and lenders to identify patterns that indicate heightened risk. These models incorporate:

- <strong>Static factors</strong>: Established risk indicators
- <strong>Dynamic factors</strong>: Real-time data for adaptive risk assessment
- <strong>Network topology</strong>: Graph-based features capturing borrower-lender relationships

<h3>Expected Impact</h3>

By providing more reliable credit risk models, this project will strengthen the P2P lending market, making it a more secure and viable alternative to traditional bank lending. The results will be valuable to:

- P2P platforms and investors
- Policymakers and regulators
- Financial institutions
- Academic researchers

</section>

---

<section id="phd-publications">
<h2>PhD Publications (ORCID 2024-2025)</h2>
<p style="font-size:0.72rem;line-height:1.25;margin:0;">
Baals, L. J., Osterrieder, J., Hadji-Misheva, B., & Liu, Y. (2024). Towards a new PhD curriculum for digital finance. <em>Open Research Europe, 4</em>, 16513. <a href="https://doi.org/10.12688/openreseurope.16513.1">https://doi.org/10.12688/openreseurope.16513.1</a><br>
Baumohl, E., Lyocsa, S., & Vasanicova, P. (2024). Macroeconomic environment and the future performance of loans: Evidence from three peer-to-peer platforms. <em>International Review of Financial Analysis, 95</em>, 103416. <a href="https://doi.org/10.1016/j.irfa.2024.103416">https://doi.org/10.1016/j.irfa.2024.103416</a><br>
Liu, Y., Baals, L. J., Osterrieder, J., & Hadji-Misheva, B. (2024). Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning. <em>Expert Systems with Applications, 252</em>, 124100. <a href="https://doi.org/10.1016/j.eswa.2024.124100">https://doi.org/10.1016/j.eswa.2024.124100</a><br>
Liu, Y., Baals, L. J., Osterrieder, J., & Hadji-Misheva, B. (2024). Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics. <em>Finance Research Letters, 63</em>, 105308. <a href="https://doi.org/10.1016/j.frl.2024.105308">https://doi.org/10.1016/j.frl.2024.105308</a><br>
Lyocsa, S., et al. (2024). Forecasting of clean energy market volatility: The role of oil and the technology sector. <em>Energy Economics</em>, 107451. <a href="https://doi.org/10.1016/j.eneco.2024.107451">https://doi.org/10.1016/j.eneco.2024.107451</a><br>
Lyocsa, S., et al. (2024). What drives the uranium sector risk? The role of attention, economic and geopolitical uncertainty. <em>Energy Economics</em>, 107980. <a href="https://doi.org/10.1016/j.eneco.2024.107980">https://doi.org/10.1016/j.eneco.2024.107980</a><br>
Lyocsa, S., et al. (2025). A fuzzy framework for realized volatility prediction. <em>Journal of Forecasting</em>. <a href="https://doi.org/10.1002/for.70082">https://doi.org/10.1002/for.70082</a><br>
Lyocsa, S., et al. (2025). Alpha-threshold networks in credit risk models. <em>Quantitative Finance</em>. <a href="https://doi.org/10.1080/14697688.2025.2465697">https://doi.org/10.1080/14697688.2025.2465697</a><br>
Lyocsa, S., et al. (2025). Do hurricanes cause storm on the stock market? <em>International Review of Financial Analysis</em>. <a href="https://doi.org/10.1016/j.irfa.2024.103816">https://doi.org/10.1016/j.irfa.2024.103816</a><br>
Osterrieder, J. (2024). A discussion paper for possible approaches to building a statistically valid backtesting framework. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4893677">https://doi.org/10.2139/ssrn.4893677</a><br>
Osterrieder, J. (2024). Consumers without credit history and ML tools. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4730445">https://doi.org/10.2139/ssrn.4730445</a><br>
Osterrieder, J. (2024). Early warning systems and customer segmentation: A systematic literature review. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4730479">https://doi.org/10.2139/ssrn.4730479</a><br>
Osterrieder, J. (2024). Enhancing security in blockchain networks: Anomalies, frauds, and advanced detection techniques. <em>arXiv</em>. <a href="https://doi.org/10.48550/arxiv.2402.11231">https://doi.org/10.48550/arxiv.2402.11231</a><br>
Osterrieder, J. (2024). Ethical artificial intelligence, fintech and data protection. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4885037">https://doi.org/10.2139/ssrn.4885037</a><br>
Osterrieder, J. (2024). Forecasting commercial customers credit risk through early warning signals data. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4754568">https://doi.org/10.2139/ssrn.4754568</a><br>
Osterrieder, J. (2024). How can artificial intelligence help customer intelligence for credit portfolio management? <em>International Journal of Information Management Data Insights</em>. <a href="https://doi.org/10.1016/j.jjimei.2024.100234">https://doi.org/10.1016/j.jjimei.2024.100234</a><br>
Osterrieder, J. (2024). Hypothesizing multimodal influence: Assessing the impact of textual and non-textual data on financial instrument pricing. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4698153">https://doi.org/10.2139/ssrn.4698153</a><br>
Osterrieder, J. (2024). Integrating early warning systems with customer segmentation. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4779632">https://doi.org/10.2139/ssrn.4779632</a><br>
Osterrieder, J. (2024). Metaverse non-fungible tokens. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4733153">https://doi.org/10.2139/ssrn.4733153</a><br>
Osterrieder, J. (2024). Modeling commodity price co-movement. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4730474">https://doi.org/10.2139/ssrn.4730474</a><br>
Osterrieder, J. (2024). Predicting retail customers' distress. <em>SSRN</em>. <a href="https://doi.org/10.2139/ssrn.4730470">https://doi.org/10.2139/ssrn.4730470</a><br>
Osterrieder, J. (2024). Stylized facts of metaverse non-fungible tokens. <em>Physica A: Statistical Mechanics and its Applications</em>. <a href="https://doi.org/10.1016/j.physa.2024.130103">https://doi.org/10.1016/j.physa.2024.130103</a><br>
Osterrieder, J. (2024). Visual XAI tool. <em>Zenodo</em>. <a href="https://doi.org/10.5281/zenodo.10934115">https://doi.org/10.5281/zenodo.10934115</a>
</p>
</section>

---

<section id="research-outputs">

<h2>Research Outputs</h2>

<p>Datasets, code, and supplementary materials deposited on Zenodo.</p>

<div class="outputs-grid">
{% for output in site.data.research_outputs %}
  <div class="output-card">
    <span class="output-type-badge">{{ output.resource_type }}</span>
    <h3><a href="{{ output.doi }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">{{ output.title }}</a></h3>
    <p class="output-creators">{{ output.creators | join: ", " }}</p>
    <p class="output-description">{{ output.description | truncate: 200 }}</p>
    <div class="output-meta">
      <span class="output-date">{{ output.publication_date }}</span>
      <a href="{{ output.doi }}" class="doi-badge" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">DOI</a>
    </div>
  </div>
{% endfor %}
</div>

</section>

---

<section id="analytics">

<h2>Research Analytics</h2>

<div class="analytics-section">
  <div class="chart-container">
    <h3>Publications by Year</h3>
    <canvas id="pubsChart"></canvas>
  </div>
  <div class="chart-container">
    <h3>Co-authorship Network</h3>
    <div id="networkGraph"></div>
  </div>
</div>

<h3>Project Timeline</h3>

<div class="timeline">
  <div class="timeline-item">
    <span class="timeline-date">Oct 2022</span>
    <div class="timeline-content">
      <strong>Project Launch</strong>
      <p>SNSF grant 205487 awarded - CHF 207,028 for network-based credit risk research</p>
    </div>
  </div>
  <div class="timeline-item">
    <span class="timeline-date">2023</span>
    <div class="timeline-content">
      <strong>Network Analysis Framework</strong>
      <p>Development of graph-based credit risk assessment methodology using Bondora P2P data</p>
    </div>
  </div>
  <div class="timeline-item">
    <span class="timeline-date">Feb 2024</span>
    <div class="timeline-content">
      <strong>Mobility Grants</strong>
      <p>Two SNSF mobility grants (CHF 40,000 total) for international collaboration</p>
    </div>
  </div>
  <div class="timeline-item">
    <span class="timeline-date">Jun 2024</span>
    <div class="timeline-content">
      <strong>Leading House Asia Grant</strong>
      <p>ETH funding (CHF 50,000) for digital assets research partnership</p>
    </div>
  </div>
  <div class="timeline-item">
    <span class="timeline-date">2024</span>
    <div class="timeline-content">
      <strong>Key Publications</strong>
      <p>Papers published in Finance Research Letters and Expert Systems with Applications</p>
    </div>
  </div>
  <div class="timeline-item">
    <span class="timeline-date">Aug 2025</span>
    <div class="timeline-content">
      <strong>Project Completion</strong>
      <p>Final deliverables and knowledge transfer to industry partners</p>
    </div>
  </div>
</div>

</section>

---

<section id="resources">

<h2>Datasets & Code</h2>

<em>Research materials and code repositories from our project</em>

<div class="resource-grid">
  <div class="resource-card">
    <h4>P2P Network Analysis Code</h4>
    <p>Python implementation of network feature extraction and credit risk modeling</p>
    <div class="resource-links">
      <a href="https://github.com/Digital-AI-Finance/network-based-credit-risk-models" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">GitHub Repository</a>
    </div>
  </div>
  <div class="resource-card">
    <h4>Bondora P2P Dataset (LoanData)</h4>
    <p>European P2P lending platform data (2009-2023) with loan performance metrics. Curated by Liu Yiting.</p>
    <div class="resource-links">
      <a href="https://osf.io/jnpfs/" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">OSF Repository</a>
      <a href="https://www.bondora.com/en/public-reports" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Data Source</a>
      <a href="https://doi.org/10.1016/j.frl.2024.105308" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Documentation</a>
    </div>
  </div>
  <div class="resource-card">
    <h4>Network Centrality Toolkit</h4>
    <p>Implementation of degree, betweenness, and eigenvector centrality for credit scoring</p>
    <div class="resource-links">
      <a href="https://doi.org/10.1016/j.eswa.2024.124100" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Related Paper</a>
    </div>
  </div>
  <div class="resource-card">
    <h4>LendingClub Dataset</h4>
    <p>US P2P lending data for comparative analysis and model validation</p>
    <div class="resource-links">
      <a href="https://www.kaggle.com/datasets/wordsforthewise/lending-club" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Kaggle Dataset</a>
    </div>
  </div>
  <div class="resource-card">
    <h4>Publications Data (JSON)</h4>
    <p>Auto-updated publication metadata from OpenAlex API</p>
    <div class="resource-links">
      <a href="https://github.com/Digital-AI-Finance/network-based-credit-risk-models/blob/main/_data/publications.json" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">View JSON</a>
      <button onclick="downloadAllBibtex()" class="resource-link">Download BibTeX</button>
    </div>
  </div>
  <div class="resource-card">
    <h4>Project Documentation</h4>
    <p>Wiki with detailed methodology, results, and supplementary materials</p>
    <div class="resource-links">
      <a href="https://github.com/Digital-AI-Finance/network-based-credit-risk-models/wiki" class="resource-link external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Project Wiki</a>
    </div>
  </div>
</div>

</section>

---

<section id="news">

<h2>News & Updates</h2>

<p class="rss-link"><a href="{{ site.baseurl }}/feed.xml" class="external-link" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">Subscribe via RSS</a></p>

<div class="news-list">
{% for item in site.data.news %}
<div class="news-item" itemscope itemtype="https://schema.org/NewsArticle">
  <span class="news-date" itemprop="datePublished">{{ item.date }}</span>
  <div class="news-content">
    <strong itemprop="headline">{{ item.title }}</strong>
    <p itemprop="description">{{ item.description }}</p>
  </div>
</div>
{% endfor %}
</div>

</section>

---

<section id="events">

<h2>Academic Events</h2>

<em>The team has received invitations to numerous international conferences, serving roles as keynote speakers, session chairs, or organizing events.</em>

<img src="images/WhatsApp_20Image_202023-09-29_20at_2015_45_edited.jpg" alt="8th Bern Conference 2024" class="event-image" loading="lazy">

<h3>8th Bern Conference 2024</h3>

<strong>September 29th, 2024</strong> - Dr. Hadji-Misheva was invited as a speaker at an inaugural research conference on Fintech and AI in Finance at the Department of Business, Bern University of Applied Science. The talk titled <em>"Leveraging Network Topology for Credit Risk Assessment"</em> explored graph-theoretical concepts and their applications for research initiatives, advancements, and innovations in credit risk scoring.

<h3>Additional Conference Presentations</h3>

<table>
  <thead>
    <tr><th>Event</th><th>Date</th><th>Location</th><th>Contribution</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>AI Finance Insights: Pioneering the Future of Fintech</strong></td><td>Sep 2024</td><td>Istanbul, Turkey</td><td>Network-Based Prediction of Loan Default Risk</td></tr>
    <tr><td><strong>COST FinAI PhD School 2024</strong></td><td>May 2024</td><td>Treviso, Italy</td><td>Workshop Organization</td></tr>
    <tr><td><strong>COST FinAI Brussels</strong></td><td>May 2024</td><td>Brussels, Belgium</td><td>Conference Organization</td></tr>
    <tr><td><strong>16th ERCIM WG / 17th CFE Conference</strong></td><td>Dec 2023</td><td>Berlin, Germany</td><td>Leveraging network topology for credit risk</td></tr>
    <tr><td><strong>8th European COST Conference on AI in Finance</strong></td><td>Sep 2023</td><td>Bern, Switzerland</td><td>Predicting Loan Default in P2P Lending</td></tr>
    <tr><td><strong>European Summer School in Financial Mathematics</strong></td><td>Sep 2023</td><td>Delft, Netherlands</td><td>Poster Presentation</td></tr>
    <tr><td><strong>COST Action Training School</strong></td><td>Jun 2023</td><td>Enschede, Netherlands</td><td>Workshop Organization</td></tr>
  </tbody>
</table>

<h3>Knowledge Transfer Events</h3>

<table>
  <thead>
    <tr><th>Event</th><th>Date</th><th>Location</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Expert Day Workshop</strong></td><td>May 2024</td><td>FHNW Campus Brugg-Windisch, Switzerland</td><td>Workshop</td></tr>
    <tr><td><strong>International Week, Shenzhen Technology University</strong></td><td>Sep 2023</td><td>Shenzhen, China</td><td>Talk</td></tr>
  </tbody>
</table>

<h3>Public Communication</h3>

<table>
  <thead>
    <tr><th>Activity</th><th>Year</th><th>Type</th><th>Reach</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Shenzhen Technology University - International Week</strong></td><td>2024</td><td>Talks/Events</td><td>International</td></tr>
    <tr><td><strong>MSCA Digital Finance</strong></td><td>2024</td><td>Webpage, New Media</td><td>International</td></tr>
    <tr><td><strong>Shenzhen Technology University - International Week</strong></td><td>2023</td><td>Talks/Events</td><td>International</td></tr>
  </tbody>
</table>

<h3>Use-Inspired Outputs</h3>

<table>
  <thead>
    <tr><th>Activity</th><th>Year</th><th>Sector</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>REA Expert Reviewer</strong></td><td>2023</td><td>European Commission</td><td>Expert reviewer for EISMEA programme</td></tr>
    <tr><td><strong>EIC Accelerator Expert</strong></td><td>2022</td><td>European Commission</td><td>EIC Work Programme evaluator</td></tr>
  </tbody>
</table>

</section>

---

<section id="collaborations">

<h2>Collaborations</h2>

<table>
  <thead>
    <tr><th>Institution</th><th>Contact</th><th>Activities</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Columbia University, USA</strong></td><td>Prof. Ali Hirsa</td><td>Constructive exchanges, Publications, Personnel exchange</td></tr>
    <tr><td><strong>American University of Sharjah, UAE</strong></td><td>Prof. Dr. Stephen Chan</td><td>Constructive exchanges, Publications, Personnel exchange</td></tr>
    <tr><td><strong>Renmin University, China</strong></td><td>Prof. Dr. Jeffrey Chu</td><td>Constructive exchanges, Publications, Personnel exchange</td></tr>
    <tr><td><strong>University of Manchester, UK</strong></td><td>Dr. Yuanyuan Zhang</td><td>Constructive exchanges, Publications</td></tr>
    <tr><td><strong>Masaryk University, Czech Republic</strong></td><td>Dr. Blanka Stadler</td><td>Constructive exchanges, Publications</td></tr>
  </tbody>
</table>

<h3>Research Networks</h3>

<strong>COST Action CA19130 - Fintech and Artificial Intelligence in Finance</strong>
- Action Chair: Joerg Osterrieder
- In-depth constructive exchanges on approaches, methods, and results
- Joint publications and personnel exchange

<strong>MSCA Industrial Doctoral Network on Digital Finance</strong>
- Coordinator: Joerg Osterrieder
- Cross-institutional research collaboration
- Doctoral training and knowledge transfer

</section>

---

<section id="funding">

<h2>Third-Party Funds</h2>

<em>The team has acquired research funds from national and international organizations, including the Swiss National Science Foundation and Horizon Europe.</em>

<div class="funding-card">
  <h3>SNSF Project Funding - Network-based Credit Risk Models (Main Grant)</h3>
  <span class="funding-amount">207,028 CHF</span>
  <dl class="funding-details">
    <dt>Grant Number</dt>
    <dd>205487</dd>
    <dt>Funding Scheme</dt>
    <dd>Weave/Lead Agency</dd>
    <dt>Grant Period</dt>
    <dd>1 October 2022 - 31 August 2025</dd>
    <dt>Institution</dt>
    <dd>Bern University of Applied Sciences (BFH)</dd>
    <dt>Title</dt>
    <dd>Network-based credit risk models in P2P lending markets</dd>
    <dt>Team</dt>
    <dd>Joerg Osterrieder (PI); Lennart Baals, Yiting Liu (Researchers)</dd>
  </dl>
</div>

<div class="funding-card">
  <h3>Leading House Asia: 2023 Call for Applied Research Partnerships, ETH</h3>
  <span class="funding-amount">50,000 CHF</span>
  <dl class="funding-details">
    <dt>Institution</dt>
    <dd>Bern University of Applied Science, CH</dd>
    <dt>Proposal Number</dt>
    <dd>FRG24-E-S25</dd>
    <dt>Grant Period</dt>
    <dd>1 June 2024 - 31 May 2025</dd>
    <dt>Title</dt>
    <dd>From Digits to Dollars: The Evolution of Price Impact in Digital Assets</dd>
    <dt>Team</dt>
    <dd>Yiting Liu (PI); Joerg Osterrieder (Co-PI)</dd>
  </dl>
</div>

<div class="funding-card">
  <h3>SNSF Mobility Grant 2024 / 1</h3>
  <span class="funding-amount">20,000 CHF</span>
  <dl class="funding-details">
    <dt>Proposal Number</dt>
    <dd>100018E_205487 / 3</dd>
    <dt>Grant Period</dt>
    <dd>1 February 2024 - 31 August 2024</dd>
    <dt>Title</dt>
    <dd>Network-based credit risk models in P2P lending markets</dd>
    <dt>Team</dt>
    <dd>Lennart John Baals (PI); Joerg Osterrieder (Co-PI)</dd>
  </dl>
</div>

<div class="funding-card">
  <h3>SNSF Mobility Grant 2024 / 2</h3>
  <span class="funding-amount">20,000 CHF</span>
  <dl class="funding-details">
    <dt>Proposal Number</dt>
    <dd>100018E_205487 / 2</dd>
    <dt>Grant Period</dt>
    <dd>1 February 2024 - 31 August 2024</dd>
    <dt>Title</dt>
    <dd>Network-based credit risk models in P2P lending markets</dd>
    <dt>Team</dt>
    <dd>Yiting Liu (PI); Joerg Osterrieder (Co-PI)</dd>
  </dl>
</div>

<div class="text-center mt-2">
  <h3>Total Funding Secured: 297,028 CHF</h3>
</div>

</section>

---

<section id="contact">

<h2>Contact Us</h2>

<div class="contact-section">

<form class="contact-form" action="https://formspree.io/f/mzzbkwqv" method="POST">
  <div class="form-group">
    <label for="name">Your Name</label>
    <input type="text" id="name" name="name" required placeholder="Enter your full name">
  </div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" required placeholder="Enter your email">
  </div>
  <div class="form-group">
    <label for="subject">Subject</label>
    <input type="text" id="subject" name="subject" required placeholder="What is this regarding?">
  </div>
  <div class="form-group">
    <label for="message">Message</label>
    <textarea id="message" name="message" required placeholder="Your message..."></textarea>
  </div>
  <button type="submit">Send Message</button>
</form>

<div class="text-center mt-2">
  <p><strong>Principal Investigator:</strong> Prof. Dr. Joerg Osterrieder</p>
  <p><strong>Institution:</strong> Bern University of Applied Sciences (BFH), Department of Business</p>
  <p><strong>Address:</strong> Bruckenstrasse 73, 3005 Bern, Switzerland</p>
</div>

</div>

</section>

---

<section id="publications">
<h2>All Publications ({{ site.data.publications | size }})</h2>
<p style="font-size:0.7rem;line-height:1.15;margin:0;"><em>Auto-updated from <a href="https://openalex.org">OpenAlex</a></em> | <button onclick="downloadAllBibtex()" style="font-size:0.7rem;padding:2px 6px;">BibTeX</button><br>
{% for pub in site.data.publications %}{{ pub.authors | truncate: 30 }} ({{ pub.year }}). {{ pub.title | truncate: 60 }}. <em>{{ pub.journal | truncate: 25 }}</em>{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">[doi]</a>{% endif %}{% if pub.citations > 0 %} [{{ pub.citations }}cit]{% endif %}<br>{% endfor %}</p>
<script>publicationsData = {{ site.data.publications | jsonify }};</script>
</section>

---

<!-- Back to Top Button -->
<button id="backToTop" class="back-to-top" onclick="scrollToTop()" aria-label="Back to top">
  &#8593;
</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>
<script src="assets/js/main.js"></script>
<script src="assets/js/visualizations.js"></script>

