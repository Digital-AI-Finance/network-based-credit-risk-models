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
    <li><a href="#research-outputs">Zenodo (12)</a></li>
    <li><a href="#analytics">Timeline</a></li>
    <div class="nav-section">Resources</div>
    <li><a href="#resources">Datasets & Code</a></li>
    <li><a href="{{ site.baseurl }}/news/">News</a></li>
    <li><a href="#events">Events</a></li>
    <div class="nav-section">Network</div>
    <li><a href="#collaborations">Collaborations</a></li>
    <li><a href="#funding">Funding</a></li>
    <li><a href="#contact">Contact</a></li>
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
    <li><a href="#research-outputs">Zenodo</a></li>
    <li><a href="#analytics">Timeline</a></li>
    <li><a href="#resources">Resources</a></li>
    <li><a href="{{ site.baseurl }}/news/">News</a></li>
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
    <span class="stat-number">247,028</span>
    <span class="stat-label">CHF Funding</span>
  </div>
  <div class="stat-item" id="totalCitations">
    <span class="stat-number">--</span>
    <span class="stat-label">Total Citations</span>
  </div>
  <div class="stat-item">
    <span class="stat-number"><a href="#research-outputs" style="color:inherit;text-decoration:none;">12</a></span>
    <span class="stat-label"><a href="#research-outputs" style="color:inherit;text-decoration:none;">Zenodo Deposits</a></span>
  </div>
  <div class="stat-item">
    <span class="stat-number">5</span>
    <span class="stat-label">Collaborations</span>
  </div>
</div>

> This SNSF-funded project develops advanced, interpretable credit risk models tailored specifically to the needs of Peer-to-Peer (P2P) lending markets using network analysis and machine learning.

</section>

---

<section id="announcement">
<h2>Project Completion Announcement</h2>
<div style="background:#f8f9fa;border-left:4px solid #0a66c2;padding:1rem;font-size:0.85rem;line-height:1.4;">
<p><strong>PROJECT COMPLETED: Network-Based Credit Risk Models in P2P Lending Markets</strong></p>
<p>I am delighted to announce the successful completion of the SNSF-funded research project (Grant 205487) on network-based credit risk models in peer-to-peer lending markets.</p>
<p><strong>What we achieved:</strong> Over three years (Oct 2022 - Aug 2025), the project developed novel machine learning methodologies that leverage network topology to assess credit risk in P2P lending. The supervised network-based approach fundamentally advances how we understand borrower relationships and default prediction.</p>
<p><strong>Key outcomes:</strong> 12 open-access Zenodo deposits | 2 PhD researchers trained | CHF 247,028 total funding | Publications in Expert Systems with Applications, Finance Research Letters, Quantitative Finance, Energy Economics</p>
<p><strong>Core team:</strong> <a href="https://www.linkedin.com/in/lennart-john-baals-a621aa193/">@Lennart John Baals</a> | <a href="https://www.linkedin.com/in/yiting-liu-313587266/">@Yiting Liu</a> | <a href="https://www.linkedin.com/in/hadjimisheva/">@Branka Hadji Misheva</a> | @Stefan Lyocsa</p>
<p><strong>International collaborators:</strong> @Ali Hirsa (Columbia) | @Stephen Chan (AUS) | @Jeffrey Chu (Renmin) | @Yuanyuan Zhang (Manchester) | @Blanka Stadler (Masaryk)</p>
<p><strong>Institutions:</strong> <a href="https://www.bfh.ch">@BFH</a> | <a href="https://www.utwente.nl">@University of Twente</a> | <a href="https://www.snf.ch">@SNSF</a> | <a href="https://www.cost.eu">@COST Association</a></p>
<p>The research demonstrates that network position contains genuine predictive signal for default risk. A key finding: simple degree centrality often matches complex metrics like PageRank, offering practitioners an accessible entry point to network-based credit assessment.</p>
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

---

<section id="research-outputs">

<h2>Open Access Research Outputs (Zenodo)</h2>

<div style="background:linear-gradient(135deg,#1e3a5f,#2d5a8f);color:white;padding:1rem;border-radius:8px;margin-bottom:1rem;">
<p style="margin:0;font-size:0.85rem;"><strong>12 Open-Access Deposits</strong> | All research materials freely available under CC-BY or MIT license</p>
</div>

<div style="font-size:0.75rem;line-height:1.4;">
<p style="margin:0.5rem 0;"><strong>Working Papers & Journal Articles:</strong></p>
<ol style="margin:0;padding-left:1.5rem;">
<li><a href="https://zenodo.org/records/17991107" target="_blank">Leveraging Network Topology for Credit Risk Assessment in P2P Lending</a> - Expert Systems with Applications code/data <a href="https://doi.org/10.5281/zenodo.17991107">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17990873" target="_blank">Network Evidence on Credit-Risk Pricing in P2P Lending</a> - PhD Chapter 4 <a href="https://doi.org/10.5281/zenodo.17990873">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17990398" target="_blank">State-Dependent Pricing in FinTech Credit: Evidence from P2P Lending</a> - PhD Chapter 5 <a href="https://doi.org/10.5281/zenodo.17990398">[DOI]</a></li>
</ol>

<p style="margin:0.5rem 0;"><strong>Reproducible Code & Data (Yiting Liu):</strong></p>
<ol start="4" style="margin:0;padding-left:1.5rem;">
<li><a href="https://zenodo.org/records/17989119" target="_blank">Code: Network centrality and credit risk (Finance Research Letters)</a> <a href="https://doi.org/10.5281/zenodo.17989119">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17990581" target="_blank">Code: Leveraging network topology (Expert Systems with Applications)</a> <a href="https://doi.org/10.5281/zenodo.17990581">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17990002" target="_blank">Code: Credit Risk via GNN with Homophily-Guided Graph Construction</a> <a href="https://doi.org/10.5281/zenodo.17990002">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17990140" target="_blank">Code: Tree-based Interpretation Framework for R2-RD Models</a> <a href="https://doi.org/10.5281/zenodo.17990140">[DOI]</a></li>
</ol>

<p style="margin:0.5rem 0;"><strong>Conference Presentations (Lennart John Baals):</strong></p>
<ol start="8" style="margin:0;padding-left:1.5rem;">
<li><a href="https://zenodo.org/records/17964900" target="_blank">COST FinAI Meets Istanbul Conference (May 2024)</a> <a href="https://doi.org/10.5281/zenodo.17964900">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17992322" target="_blank">4th Int'l Symposium on Big Data and AI, Hong Kong (Dec 2024)</a> - SLR on Graph-Based Credit Models <a href="https://doi.org/10.5281/zenodo.17992322">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17992484" target="_blank">Bern Conference 2023</a> - Network Topology for Credit Risk <a href="https://doi.org/10.5281/zenodo.17992484">[DOI]</a></li>
<li><a href="https://zenodo.org/records/17992591" target="_blank">BFH Doctoral Seminar (Nov 2023)</a> - Identifying Mispriced Loans <a href="https://doi.org/10.5281/zenodo.17992591">[DOI]</a></li>
</ol>

<p style="margin:0.5rem 0;"><strong>Academic Records:</strong></p>
<ol start="12" style="margin:0;padding-left:1.5rem;">
<li><a href="https://zenodo.org/records/17992215" target="_blank">PhD Qualifier Report and Presentation</a> - University of Twente <a href="https://doi.org/10.5281/zenodo.17992215">[DOI]</a></li>
</ol>
</div>

</section>

---

<section id="analytics">

<h2>Project Timeline</h2>

<div style="overflow-x:auto;padding:1rem 0;">
<div style="display:flex;min-width:2400px;position:relative;">
<!-- Timeline line -->
<div style="position:absolute;top:50%;left:0;right:0;height:3px;background:linear-gradient(90deg,#1e3a5f,#c5a028);z-index:0;"></div>

<!-- 2022 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:12px;height:12px;background:#1e3a5f;border-radius:50%;margin:0 auto;border:2px solid #c5a028;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Oct 2022</strong><br>Project Launch<br><span style="color:#666;">SNSF CHF 207k</span></div>
</div>

<!-- Jun 2023 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Jun 2023</strong><br>Training School<br><span style="color:#666;">Enschede</span></div>
</div>

<!-- Sep 2023 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Sep 2023</strong><br>COST Conference<br><span style="color:#666;">Bern</span></div>
</div>

<!-- Sep 2023 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Sep 2023</strong><br>Summer School<br><span style="color:#666;">Delft</span></div>
</div>

<!-- Nov 2023 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Nov 2023</strong><br>BFH Seminar<br><span style="color:#666;"><a href="https://zenodo.org/records/17992591">Zenodo</a></span></div>
</div>

<!-- Dec 2023 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Dec 2023</strong><br>ERCIM/CFE<br><span style="color:#666;">Berlin</span></div>
</div>

<!-- Feb 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:12px;height:12px;background:#c5a028;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Feb 2024</strong><br>Mobility Grants<br><span style="color:#666;">CHF 40k</span></div>
</div>

<!-- Mar 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#22c55e;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Mar 2024</strong><br>Zenodo: FRL Code<br><span style="color:#666;"><a href="https://zenodo.org/records/17989119">Liu</a></span></div>
</div>

<!-- May 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>May 2024</strong><br>PhD School<br><span style="color:#666;">Treviso</span></div>
</div>

<!-- May 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#d62728;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>May 2024</strong><br>FRL Paper<br><span style="color:#666;"><a href="https://doi.org/10.1016/j.frl.2024.105308">DOI</a></span></div>
</div>

<!-- May 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#22c55e;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>May 2024</strong><br>Zenodo: ESWA<br><span style="color:#666;"><a href="https://zenodo.org/records/17990581">Liu</a></span></div>
</div>

<!-- Sep 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Sep 2024</strong><br>AI Finance<br><span style="color:#666;">Istanbul</span></div>
</div>

<!-- Oct 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#d62728;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Oct 2024</strong><br>ESWA Paper<br><span style="color:#666;"><a href="https://doi.org/10.1016/j.eswa.2024.124100">DOI</a></span></div>
</div>

<!-- Oct 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#22c55e;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Oct 2024</strong><br>Zenodo: Istanbul<br><span style="color:#666;"><a href="https://zenodo.org/records/17964900">Baals</a></span></div>
</div>

<!-- Dec 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#2d5a8f;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Dec 2024</strong><br>Big Data & AI<br><span style="color:#666;">Hong Kong</span></div>
</div>

<!-- Dec 2024 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#22c55e;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Dec 2024</strong><br>Zenodo: 8 deposits<br><span style="color:#666;"><a href="#research-outputs">View all</a></span></div>
</div>

<!-- 2025 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:10px;height:10px;background:#d62728;border-radius:50%;margin:0 auto;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>2025</strong><br>Quant Finance<br><span style="color:#666;"><a href="https://doi.org/10.1080/14697688.2025.2465697">DOI</a></span></div>
</div>

<!-- Aug 2025 -->
<div style="flex:1;text-align:center;position:relative;z-index:1;">
<div style="width:14px;height:14px;background:#22c55e;border-radius:50%;margin:0 auto;border:2px solid #1e3a5f;"></div>
<div style="font-size:0.65rem;margin-top:0.3rem;"><strong>Aug 2025</strong><br>PROJECT COMPLETE<br><span style="color:#666;">12 Zenodo deposits</span></div>
</div>

</div>
</div>

<div style="display:flex;gap:1rem;justify-content:center;font-size:0.7rem;margin-top:0.5rem;">
<span><span style="display:inline-block;width:10px;height:10px;background:#1e3a5f;border-radius:50%;"></span> Milestone</span>
<span><span style="display:inline-block;width:10px;height:10px;background:#c5a028;border-radius:50%;"></span> Funding</span>
<span><span style="display:inline-block;width:10px;height:10px;background:#d62728;border-radius:50%;"></span> Publication</span>
<span><span style="display:inline-block;width:10px;height:10px;background:#22c55e;border-radius:50%;"></span> Zenodo</span>
<span><span style="display:inline-block;width:10px;height:10px;background:#2d5a8f;border-radius:50%;"></span> Conference</span>
</div>

</section>

---

<section id="resources">

<h2>Datasets & Code</h2>

<em>Research materials and code repositories from the project</em>

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

<p><a href="{{ site.baseurl }}/news/" style="font-weight:600;">View All News (30+ items) &rarr;</a> | <a href="{{ site.baseurl }}/feed.xml">RSS</a></p>

<div style="font-size:0.8rem;">
{% for item in site.data.news limit:3 %}
<div style="border-left:3px solid #1e3a5f;padding-left:0.75rem;margin:0.5rem 0;">
<strong>{{ item.date }}</strong> - {{ item.title }}<br>
<span style="color:#666;">{{ item.description | truncate: 120 }}</span>
</div>
{% endfor %}
</div>

<p><a href="{{ site.baseurl }}/news/">See all news, publications, conferences, and Zenodo releases &rarr;</a></p>

</section>

---

<section id="events">

<h2>Academic Events</h2>

<em>The team has received invitations to numerous international conferences, serving roles as keynote speakers, session chairs, or organizing events.</em>

<h3>Conference Presentations</h3>

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
  <h3>Total Funding Secured: 247,028 CHF</h3>
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

