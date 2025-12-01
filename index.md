---
layout: default
title: Network-Based Credit Risk Models in P2P Lending Markets
---

<nav class="nav-container">
  <ul class="nav-menu">
    <li><a href="#home">Home</a></li>
    <li><a href="#team">Team</a></li>
    <li><a href="#research">Research</a></li>
    <li><a href="#publications">Publications</a></li>
    <li><a href="#events">Events</a></li>
    <li><a href="#collaborations">Collaborations</a></li>
    <li><a href="#funding">Funding</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<section id="home">

<div class="logo-banner">
  <img src="assets/images/logos/snsf-logo.svg" alt="Swiss National Science Foundation">
  <img src="assets/images/logos/bfh-logo.svg" alt="Bern University of Applied Sciences">
</div>

<div class="stats-banner">
  <div class="stat-item">
    <span class="stat-number">90,000</span>
    <span class="stat-label">CHF Funding</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">{{ site.data.publications | size }}</span>
    <span class="stat-label">Publications</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">6</span>
    <span class="stat-label">Collaborations</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">4</span>
    <span class="stat-label">Researchers</span>
  </div>
</div>

> This SNSF-funded project develops advanced, interpretable credit risk models tailored specifically to the needs of Peer-to-Peer (P2P) lending markets using network analysis and machine learning.

</section>

---

<section id="team">

## Our Team

*International cooperation between Bern Business School (Switzerland) and partner institutions*

<div class="team-grid">

<div class="team-card">
  <img src="images/Osterrieder.jpg" alt="Joerg Osterrieder">
  <span class="role-badge">Principal Investigator</span>
  <h4>Prof. Dr. Joerg Osterrieder</h4>
  <p class="institution">Bern Business School, Switzerland<br>University of Twente, Netherlands</p>
</div>

<div class="team-card">
  <img src="images/Baals_JPG.jpg" alt="Lennart John Baals">
  <span class="role-badge">Researcher</span>
  <h4>Lennart John Baals</h4>
  <p class="institution">Bern Business School, Switzerland<br>University of Twente, Netherlands</p>
</div>

<div class="team-card">
  <img src="images/Hadji_20Misheva.jpg" alt="Branka Hadji Misheva">
  <span class="role-badge">Researcher</span>
  <h4>Prof. Dr. Branka Hadji Misheva</h4>
  <p class="institution">Bern Business School, Switzerland</p>
</div>

<div class="team-card">
  <img src="images/Liu_20Yiting.jpg" alt="Yiting Liu">
  <span class="role-badge">Researcher</span>
  <h4>Dr. Yiting Liu</h4>
  <p class="institution">Bern Business School, Switzerland<br>University of Twente, Netherlands</p>
</div>

</div>

</section>

---

<section id="research">

## Research Project

### Background

Peer-to-peer (P2P) lending has become an increasingly popular alternative to traditional bank lending, allowing individuals and businesses to borrow money directly from investors through online platforms without involving banks. While this method offers advantages such as higher returns for investors and greater access to credit for borrowers, it also brings unique risks. The decentralized nature of P2P lending means that loans are funded entirely by investors, without the safeguards of bank intermediation.

### Rationale

The growing presence of P2P lending markets, especially during economic crises, exposes these platforms to significant risks, including adverse selection and moral hazard. Unlike traditional banks that use long-term relationships and extensive data to evaluate borrowers, P2P platforms have less detailed information and face higher levels of uncertainty. There is a critical need for robust credit risk models that can accurately assess the creditworthiness of borrowers in these markets.

### Objectives

This project aims to develop **advanced, interpretable credit risk models** tailored specifically to the needs of P2P lending markets. These models will address the unique challenges of P2P lending, such as:

- Higher information asymmetry
- Less regulation compared to traditional banking
- Increased risk during economic downturns

The ultimate goal is to enhance trust between investors and P2P platforms by providing accurate tools for evaluating and mitigating credit risk.

### Methods

The project develops credit risk models using **network-based approaches**, analyzing the connections between borrowers and lenders to identify patterns that indicate heightened risk. These models incorporate:

- **Static factors**: Established risk indicators
- **Dynamic factors**: Real-time data for adaptive risk assessment
- **Network topology**: Graph-based features capturing borrower-lender relationships

### Expected Impact

By providing more reliable credit risk models, this project will strengthen the P2P lending market, making it a more secure and viable alternative to traditional bank lending. The results will be valuable to:

- P2P platforms and investors
- Policymakers and regulators
- Financial institutions
- Academic researchers

</section>

---

<section id="publications">

## Scientific Publications

*Auto-updated from [OpenAlex.org](https://openalex.org) - {{ site.data.publications | size }} publications*

<div class="publication-list">
{% for pub in site.data.publications limit:20 %}
<div class="pub-item">
  <div class="pub-title">{{ pub.title }}</div>
  <div class="pub-meta">{{ pub.authors }} ({{ pub.year }}) - <em>{{ pub.journal }}</em></div>
  <div class="pub-badges">
    {% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}" class="doi-link" target="_blank">DOI</a>{% endif %}
    {% if pub.citations > 0 %}<span class="citations-badge">{{ pub.citations }} citations</span>{% endif %}
    {% if pub.open_access %}<span class="citations-badge">Open Access</span>{% endif %}
  </div>
</div>
{% endfor %}
</div>

{% if site.data.publications.size > 20 %}
<p class="text-center"><em>Showing 20 of {{ site.data.publications | size }} publications. <a href="https://openalex.org/authors/A5047295072">View all on OpenAlex</a></em></p>
{% endif %}

</section>

---

<section id="events">

## Academic Events

*The team has received invitations to numerous international conferences, serving roles as keynote speakers, session chairs, or organizing events.*

<img src="images/WhatsApp_20Image_202023-09-29_20at_2015_45_edited.jpg" alt="8th Bern Conference 2024" class="event-image">

### 8th Bern Conference 2024

**September 29th, 2024** - Dr. Hadji-Misheva was invited as a speaker at an inaugural research conference on Fintech and AI in Finance at the Department of Business, Bern University of Applied Science. The talk titled *"Leveraging Network Topology for Credit Risk Assessment"* explored graph-theoretical concepts and their applications for research initiatives, advancements, and innovations in credit risk scoring.

</section>

---

<section id="collaborations">

## Collaborations

| Institution | Contact | Activities |
|-------------|---------|------------|
| **American University of Sharjah, UAE** | Prof. Dr. Stephen Chan | Constructive exchanges, Publications, Personnel exchange |
| **University of Manchester, UK** | Dr. Yuanyuan Zhang | Constructive exchanges, Publications |
| **Renmin University, China** | Prof. Dr. Jeffrey Chu | Constructive exchanges, Publications |
| **Bern Business School, Switzerland** | Prof. Dr. Branka Hadji Misheva | Constructive exchanges, Publications, Personnel exchange |

### Research Networks

**COST Action CA19130 - Fintech and Artificial Intelligence in Finance**
- Action Chair: Joerg Osterrieder
- In-depth constructive exchanges on approaches, methods, and results
- Joint publications and personnel exchange

**MSCA Industrial Doctoral Network on Digital Finance**
- Coordinator: Joerg Osterrieder
- Cross-institutional research collaboration
- Doctoral training and knowledge transfer

</section>

---

<section id="funding">

## Third-Party Funds

*The team has acquired research funds from national and international organizations, including the Swiss National Science Foundation and Horizon Europe.*

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
  <h3>Total Funding Secured: 90,000 CHF</h3>
</div>

</section>

---

<section id="contact">

## Contact Us

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

<footer class="site-footer">
  <div class="footer-content">
    <div>
      <p>&copy; 2025 Digital AI Finance Research Group</p>
      <p>Source: <a href="https://www.digital-finance-msca.com/network-based-credit-risk-models-snsf">digital-finance-msca.com</a></p>
    </div>
    <div class="footer-links">
      <a href="https://github.com/Digital-AI-Finance/network-based-credit-risk-models">GitHub</a>
      <a href="https://github.com/Digital-AI-Finance/network-based-credit-risk-models/wiki">Wiki</a>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
