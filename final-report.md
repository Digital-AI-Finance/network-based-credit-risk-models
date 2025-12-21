---
layout: default
title: Final Scientific Report
permalink: /final-report/
description: SNSF Final Scientific Report for Project 205487 - Network-Based Credit Risk Models in P2P Lending Markets
---

<style>
.report-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem 1rem;
}
.report-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 3px solid var(--gold);
}
.report-header h1 {
  font-size: 1.8rem;
  color: var(--navy);
  margin-bottom: 0.5rem;
}
.report-header .subtitle {
  font-size: 1.2rem;
  color: var(--gold);
  margin-bottom: 1.5rem;
}
.snsf-meta-table {
  margin: 1rem auto;
  border-collapse: collapse;
  text-align: left;
}
.snsf-meta-table td {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
}
.snsf-meta-table td:first-child {
  font-weight: 600;
  color: var(--navy);
  background: var(--gold-light);
  min-width: 150px;
}
.section-header {
  background: linear-gradient(135deg, var(--navy), var(--navy-secondary));
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 8px 8px 0 0;
  margin-top: 2.5rem;
}
.section-header h2 {
  margin: 0;
  font-size: 1.1rem;
}
.section-content {
  background: white;
  padding: 1.5rem;
  border: 1px solid #e0e0e0;
  border-top: none;
  border-radius: 0 0 8px 8px;
  line-height: 1.7;
}
.objective-box {
  background: var(--gold-light);
  border-left: 4px solid var(--gold);
  padding: 1rem 1.5rem;
  margin: 1rem 0;
  border-radius: 0 8px 8px 0;
}
.objective-box h4 {
  color: var(--navy);
  margin: 0 0 0.5rem 0;
  font-size: 0.95rem;
}
.achievement-tag {
  display: inline-block;
  background: #22c55e;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.additional-outcomes {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px dashed var(--gold);
}
.additional-outcomes h3 {
  color: var(--navy);
  font-size: 1rem;
  margin-bottom: 1rem;
}
/* Collapsible Extended Section */
.extended-info {
  margin-top: 3rem;
  border: 2px solid var(--gold);
  border-radius: 8px;
}
.extended-info summary {
  background: var(--gold-light);
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-weight: 600;
  color: var(--navy);
  font-size: 1.1rem;
  border-radius: 6px;
  list-style: none;
}
.extended-info summary::-webkit-details-marker {
  display: none;
}
.extended-info summary::before {
  content: "+ ";
  font-weight: bold;
}
.extended-info[open] summary::before {
  content: "- ";
}
.extended-info[open] summary {
  border-bottom: 1px solid var(--gold);
  border-radius: 6px 6px 0 0;
}
.extended-info .extended-content {
  padding: 1.5rem;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.stat-card {
  background: linear-gradient(135deg, var(--navy), var(--navy-secondary));
  color: white;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
}
.stat-card .number {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--gold);
}
.stat-card .label {
  font-size: 0.8rem;
  opacity: 0.9;
}
.appendix-section {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid var(--gold-light);
}
.pub-item {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin: 1rem 0;
}
.pub-item h4 {
  color: var(--navy);
  margin: 0 0 0.5rem 0;
  font-size: 0.95rem;
}
.pub-meta {
  font-size: 0.85rem;
  color: #666;
}
.zenodo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}
.zenodo-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1rem;
}
.zenodo-card h4 {
  font-size: 0.9rem;
  color: var(--navy);
  margin: 0 0 0.5rem 0;
  line-height: 1.4;
}
.zenodo-card .type-badge {
  display: inline-block;
  background: var(--gold-light);
  color: var(--navy);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.event-list {
  list-style: none;
  padding: 0;
}
.event-list li {
  padding: 0.75rem 0;
  border-bottom: 1px solid #eee;
  display: flex;
  gap: 1rem;
}
.event-list .date {
  min-width: 100px;
  color: var(--gold);
  font-weight: 600;
  font-size: 0.85rem;
}
.event-list .details {
  flex: 1;
}
.event-list .location {
  font-size: 0.85rem;
  color: #666;
}
.badge {
  background: var(--gold);
  color: var(--navy);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
}
@media (max-width: 768px) {
  .snsf-meta-table {
    width: 100%;
  }
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

<div class="report-container">

<div class="report-header">
<h1>Final Scientific Report</h1>
<div class="subtitle">Network-Based Credit Risk Models in P2P Lending Markets</div>

<table class="snsf-meta-table">
<tr>
<td>Name</td>
<td>Prof. Dr. Joerg Osterrieder</td>
</tr>
<tr>
<td>Project number</td>
<td>205487</td>
</tr>
</table>
</div>

<!-- Section 1.1: Achievement of research objectives (mandatory) -->
<div class="section-header">
<h2>1.1 Achievement of research objectives (mandatory)</h2>
</div>
<div class="section-content">

<p><strong>Main Objective:</strong> To advance our understanding of credit risk modeling in P2P lending markets by designing and empirically verifying new network-based credit risk models. This project has attributes of a methodological and empirical project with practical impact, addressing information asymmetry inherent in P2P lending through network analysis.</p>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Contribution 1 (Methodological): Supervised Network-Based Credit Risk Models</h4>
<p>Previous methods (Ahelegbey et al., 2019; Giudici et al., 2019, 2020) ignored loan status, leading to unsupervised network-based learning. Our approach utilizes class information (loan default status) to construct supervised networks, as supervised learning generally outperforms unsupervised approaches. We developed a two-step machine learning methodology that constructs borrower similarity graphs and extracts multiple centrality measures (PageRank, betweenness, closeness, Katz, hub/authority) as predictive features.</p>
<p><strong>Evidence:</strong> Liu et al. (2024), "Leveraging network topology for credit risk assessment in P2P lending," <em>Expert Systems with Applications</em>, Vol. 252, Article 124100. <strong>17 citations.</strong></p>
</div>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Contribution 2 (Methodological): Cross-Validation for Network Hyperparameters</h4>
<p>In contrast to previous studies, our work acknowledges that network creation and feature extraction depend on hyperparameters. We applied cross-validation to tune network hyperparameters and resulting features, including similarity thresholds, k-nearest-neighbor connection rules, and centrality measure configurations. This systematic approach to hyperparameter optimization contrasts with prior work that used fixed, ad-hoc parameter choices.</p>
<p><strong>Evidence:</strong> Methods sections in Liu et al. (2024) ESWA and FRL publications; hyperparameter sensitivity analysis in Zenodo deposits.</p>
</div>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Contribution 3 (Methodological): Multiple Networks with Bootstrap Aggregation</h4>
<p>Previous studies created only one network. We designed methods to create multiple networks that: (i) utilize different (random) sets of variables, and (ii) rely on bootstrap aggregation (bagging). This directly addresses data noisiness, which is ignored in existing literature. The approach was validated using Elastic Net, Random Forest, Multi-Layer Perceptron, and XGBoost ensemble methods.</p>
<p><strong>Evidence:</strong> Ensemble methodology in publications; robustness checks using shuffled centrality features confirmed predictive value.</p>
</div>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Contribution 4 (Empirical): Validation Across Multiple P2P Datasets</h4>
<p>We enriched the empirical literature (most studies use fewer than two datasets) by validating models across different market platforms. Primary analysis used the Bondora dataset (231,039 borrowers, 112 variables, European P2P market), with comparative validation using LendingClub data (US market). This enabled observation of credit drivers across platforms with different geographic and regulatory characteristics.</p>
<p><strong>Evidence:</strong> Liu et al. (2024), "Network centrality and credit risk," <em>Finance Research Letters</em>, Vol. 63, Article 105308. <strong>11 citations.</strong></p>
</div>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Contribution 5 (Practical): Explainable AI for Interpretable Credit Risk Models</h4>
<p>We investigated the applicability of XAI methods (SHAP, LIME) to credit scoring models, enabling estimation of both global effects (expected effect of each variable on outcome) and local effects (expected effect of each variable for a specific individual loan). This addresses regulatory requirements for interpretable automated lending decisions (GDPR, policymaker trends). Surrogate decision trees and manual tree-based interpretation frameworks were developed for regime detection models.</p>
<p><strong>Evidence:</strong> SHAP explainability notebooks in Zenodo deposit 17991107; tree-based interpretation framework in Zenodo deposit 17990398; 12 Zenodo deposits ensuring reproducibility.</p>
</div>

<div class="additional-outcomes">
<h3>Additional Project Outcomes</h3>

<div class="objective-box">
<span class="achievement-tag">ACHIEVED</span>
<h4>Research Capacity Building and International Collaboration</h4>
<p>The project trained two PhD researchers (Lennart John Baals and Yiting Liu) who developed expertise in digital finance, network modeling, and explainable AI. We established collaborations with five international institutions across four continents (Masaryk University, Columbia University, American University of Sharjah, Renmin University of China, University of Manchester). The PI serves as Action Chair of COST Action CA19130 (Fintech and AI in Finance) and Coordinator of the MSCA Industrial Doctoral Network on Digital Finance.</p>
</div>

<p><strong>Additional Funding Secured:</strong> The project's success attracted CHF 90,000 in additional funding: two SNSF Mobility Grants (CHF 20,000 each) and a Leading House Asia grant (CHF 50,000) for related digital assets research.</p>
</div>

</div>

<!-- Section 1.2: Challenges, negative results and unexpected outcomes -->
<div class="section-header">
<h2>1.2 Challenges, negative results and unexpected outcomes</h2>
</div>
<div class="section-content">

<p><strong>Data Access Challenges:</strong> The original proposal planned validation across 7 P2P platforms (Lending Club, Prosper, Zopa, Mintos, Bondora, Home Credit, Kiva). Due to data access restrictions, platform terms of service (e.g., Bondora section 13.4 preventing redistribution), and proprietary data policies, we focused primary empirical analysis on Bondora (European) with comparative validation using LendingClub (US), providing geographic and regulatory diversity. This led us to focus on reproducible code and documentation in our Zenodo deposits.</p>

<p><strong>Platform Evolution:</strong> The P2P lending landscape evolved significantly during the project period, with some platforms reducing operations or changing data policies. Several planned data sources became unavailable or restricted. This required flexibility in our empirical strategy, ultimately strengthening our focus on methodological contributions applicable across different platforms.</p>

<p><strong>Computational Scaling:</strong> Network construction for large loan portfolios presented computational challenges. We addressed this through efficient similarity thresholding and k-nearest-neighbor connection rules to maintain connectivity while managing graph size.</p>

<p><strong>Unexpected Finding:</strong> Our analysis revealed that network position (degree centrality) alone provides substantial predictive power, sometimes matching or exceeding more complex centrality measures. This simplified insight has practical implications for platform operators seeking interpretable risk indicators.</p>

</div>

<!-- Section 1.3: Contribution to knowledge advancement -->
<div class="section-header">
<h2>1.3 Contribution to knowledge advancement</h2>
</div>
<div class="section-content">

<p><strong>Methodological Contribution:</strong> We established network topology as a viable and valuable feature source for credit risk modeling in P2P lending. Our two-step ML approach provides a replicable framework for combining structural and attribute-based predictors. The systematic literature review (78 articles analyzed) provides a comprehensive synthesis of graph-based credit modeling approaches.</p>

<p><strong>Practical Impact:</strong> Our models and code are directly applicable to P2P lending platforms for risk assessment. The interpretability framework using SHAP/LIME enables platform operators to explain credit decisions to borrowers and regulators, addressing transparency requirements in automated lending decisions.</p>

<p><strong>Open Science Contribution:</strong> All 12 Zenodo deposits (100% open access) ensure complete reproducibility of our findings. The deposits include LaTeX sources, Jupyter notebooks, Python/R scripts, and comprehensive documentation, enabling other researchers to validate, extend, and build upon our work.</p>

<p><strong>Capacity Building:</strong> Two PhD researchers were trained in cutting-edge methods at the intersection of network science, machine learning, and finance. Knowledge transfer activities included an Expert Day workshop at FINMA (Swiss financial regulator) and presentations at international research events in eight countries.</p>

<p><strong>Research Network Leadership:</strong> The PI's roles as COST Action Chair and MSCA Network Coordinator enabled broad dissemination of project findings across 40+ European institutions, creating lasting infrastructure for fintech research collaboration.</p>

</div>

<!-- Collapsible Extended Project Information -->
<details class="extended-info">
<summary>Extended Project Information</summary>
<div class="extended-content">

<!-- Project Statistics -->
<h3 style="color: var(--navy); margin-top: 0;">Project Statistics</h3>
<div class="stats-grid">
<div class="stat-card">
<div class="number">6+</div>
<div class="label">Core Publications</div>
</div>
<div class="stat-card">
<div class="number">28+</div>
<div class="label">Citations Received</div>
</div>
<div class="stat-card">
<div class="number">12</div>
<div class="label">Zenodo Deposits</div>
</div>
<div class="stat-card">
<div class="number">8</div>
<div class="label">Conference Presentations</div>
</div>
<div class="stat-card">
<div class="number">2</div>
<div class="label">PhD Researchers Trained</div>
</div>
<div class="stat-card">
<div class="number">CHF 90k</div>
<div class="label">Additional Funding</div>
</div>
</div>

<!-- Executive Summary -->
<div class="appendix-section">
<h3>Executive Summary</h3>

<p>This Final Scientific Report documents the successful completion of SNSF Project 205487 "Network-Based Credit Risk Models in P2P Lending Markets" (October 2022 - August 2025). The project achieved all its research objectives, producing significant methodological innovations and empirical contributions to the field of digital finance.</p>

<p><strong>Key Achievements:</strong></p>
<ul>
<li><strong>Novel Methodology:</strong> Developed a two-step machine learning approach combining network centrality metrics with traditional credit risk factors, demonstrating that borrower network position significantly influences default probability</li>
<li><strong>High-Impact Publications:</strong> 4 peer-reviewed journal articles (17+ and 11+ citations) plus 2 submitted manuscripts, all open access</li>
<li><strong>Open Science:</strong> 12 Zenodo deposits ensuring full reproducibility; dataset archived on OSF</li>
<li><strong>Capacity Building:</strong> Trained 2 PhD researchers; established collaborations with 5 international institutions across 4 continents</li>
<li><strong>Additional Funding:</strong> Attracted CHF 90,000 in follow-on grants (SNSF Mobility, Leading House Asia)</li>
<li><strong>Policy Engagement:</strong> FINMA Expert Day workshop; leadership of COST Action CA19130 and MSCA Digital Finance Network</li>
</ul>

<p><strong>Original Research Objectives (from Grant Proposal):</strong></p>
<ol>
<li>Develop advanced, interpretable credit risk models tailored to P2P lending markets</li>
<li>Test and compare usefulness of network-enhanced models with real P2P datasets</li>
<li>Address higher information asymmetry in P2P platforms through network analysis</li>
<li>Incorporate inter-entity relationships to assess risk transmission</li>
<li>Create state-of-the-art models for P2P platforms characterized by loose regulation</li>
<li>Enhance trust between investors and P2P platforms</li>
</ol>

<p>All objectives were achieved, as documented in Section 1.1 above with evidence from peer-reviewed publications and open science deposits.</p>
</div>

<!-- Section 1.4: Impact Statement -->
<div class="appendix-section">
<h3>1.4 Impact Statement</h3>

<p>This section addresses the impact and outcomes of the research, as recommended by <a href="https://www.snf.ch/en/eBcE6xqoFI2PAqhI/page/funding/regulations-whats-new" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF 2025 reporting best practices</a>.</p>

<div class="objective-box">
<h4>Scientific Impact</h4>
<p>Our publications have received <strong>28+ citations</strong> within 12 months of publication, indicating rapid adoption by the research community. The two-step ML methodology combining network centrality with traditional credit features has been referenced in subsequent studies on P2P lending risk assessment. The systematic literature review provides a foundational reference for researchers entering the field of graph-based credit modeling.</p>
</div>

<div class="objective-box">
<h4>Economic Impact</h4>
<p>The developed models and open-source code are directly applicable to P2P lending platforms for improved credit risk assessment. By enabling more accurate default prediction, platforms can better price loans, reduce losses, and offer more competitive rates to creditworthy borrowers. The interpretability framework (SHAP/LIME) addresses regulatory requirements for explainable automated decisions in lending.</p>
</div>

<div class="objective-box">
<h4>Social Impact</h4>
<p>Improved credit risk models contribute to financial inclusion by enabling P2P platforms to serve borrowers who may be underserved by traditional banking. Better risk assessment reduces adverse selection, protecting retail investors who fund P2P loans. The transparency framework enhances borrower trust in automated credit decisions.</p>
</div>

<div class="objective-box">
<h4>Policy Impact</h4>
<p>The project engaged directly with financial regulators through the <strong>FINMA Expert Day</strong> workshop (May 2024), presenting research findings to Swiss financial supervisory staff. The PI's leadership of COST Action CA19130 facilitated policy discussions at EU level, including events in Brussels addressing AI in finance policy implications.</p>
</div>

<div class="objective-box">
<h4>Educational Impact</h4>
<p>The project trained <strong>2 PhD researchers</strong> in cutting-edge methods at the intersection of network science, machine learning, and finance. The publication "Towards a new PhD Curriculum for Digital Finance" (Open Research Europe, 2024) disseminates best practices for doctoral training in this emerging field. Research was presented at 8 international academic events across 8 countries.</p>
</div>
</div>

<!-- Section 1.5: Sustainability Plan -->
<div class="appendix-section">
<h3>1.5 Sustainability Plan</h3>

<p>This section addresses the long-term sustainability and preservation of research outputs, as recommended by <a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF lifetime management best practices</a>.</p>

<div class="objective-box">
<h4>Data Preservation</h4>
<ul>
<li><strong>Zenodo:</strong> 12 deposits archived with DOIs ensuring permanent accessibility and citability</li>
<li><strong>OSF:</strong> Curated dataset (Bondora P2P Lending) archived at <a href="https://osf.io/jnpfs/" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">https://osf.io/jnpfs/</a></li>
<li><strong>GitHub:</strong> Code repositories maintained under Digital-AI-Finance organization</li>
<li><strong>Licensing:</strong> All outputs under Creative Commons Attribution 4.0 (CC-BY 4.0)</li>
</ul>
</div>

<div class="objective-box">
<h4>Code Maintainability</h4>
<ul>
<li>All Jupyter notebooks and Python scripts include dependency specifications (requirements.txt)</li>
<li>Reproducibility verified through independent testing</li>
<li>Documentation embedded in code and supplementary README files</li>
</ul>
</div>

<div class="objective-box">
<h4>Knowledge Transfer Continuation</h4>
<ul>
<li><strong>COST Action CA19130:</strong> Fintech and AI in Finance network continues beyond project end (PI as Action Chair)</li>
<li><strong>MSCA Digital Finance Network:</strong> Industrial doctoral network continues training next-generation researchers (PI as Coordinator)</li>
<li><strong>BFH Research Group:</strong> Digital finance research continues at Bern University of Applied Sciences</li>
</ul>
</div>

<div class="objective-box">
<h4>Publication Pipeline</h4>
<ul>
<li>2 manuscripts currently under review at peer-reviewed journals</li>
<li>PhD theses in progress will generate additional publications</li>
<li>Follow-on funding (Leading House Asia, CHF 50,000) supports continued research on digital assets</li>
</ul>
</div>
</div>

<!-- Appendix A: Peer-Reviewed Publications -->
<div class="appendix-section">
<h3>Appendix A: Peer-Reviewed Publications</h3>

<div class="pub-item">
<h4>Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning</h4>
<p class="pub-meta">
<strong>Authors:</strong> Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B.<br>
<strong>Journal:</strong> Expert Systems with Applications, Vol. 252(B), Article 124100 (2024)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.1016/j.eswa.2024.124100" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.1016/j.eswa.2024.124100</a><br>
<strong>Impact:</strong> 17 citations (Scopus), 214 downloads, Open Access
</p>
</div>

<div class="pub-item">
<h4>Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics</h4>
<p class="pub-meta">
<strong>Authors:</strong> Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B.<br>
<strong>Journal:</strong> Finance Research Letters, Vol. 63, Article 105308 (2024)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.1016/j.frl.2024.105308" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.1016/j.frl.2024.105308</a><br>
<strong>Impact:</strong> 11 citations, Open Access
</p>
</div>

<div class="pub-item">
<h4>Macroeconomic environment and the future performance of loans: Evidence from three peer-to-peer platforms</h4>
<p class="pub-meta">
<strong>Authors:</strong> Baumohl, E., Lyocsa, S., Vasanicova, P.<br>
<strong>Journal:</strong> International Review of Financial Analysis, Vol. 95, Article 103416 (2024)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.1016/j.irfa.2024.103416" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.1016/j.irfa.2024.103416</a>
</p>
</div>

<div class="pub-item">
<h4>Towards a new PhD Curriculum for Digital Finance</h4>
<p class="pub-meta">
<strong>Authors:</strong> Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Liu, Y.<br>
<strong>Journal:</strong> Open Research Europe, Vol. 4, Article 16513 (2024)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.12688/openreseurope.16513.1" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.12688/openreseurope.16513.1</a><br>
<strong>Status:</strong> Published, Open Access
</p>
</div>

<h4 style="margin-top: 1.5rem; color: var(--navy);">Submitted / Under Review</h4>

<div class="pub-item" style="border-left: 3px solid var(--gold);">
<h4>Network Evidence on Credit-Risk Pricing in P2P Lending</h4>
<p class="pub-meta">
<strong>Authors:</strong> Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Gomez, L., Wang, Y.<br>
<strong>Status:</strong> SSRN Working Paper (2025)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.2139/ssrn.5276337" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.2139/ssrn.5276337</a>
</p>
</div>

<div class="pub-item" style="border-left: 3px solid var(--gold);">
<h4>State-Dependent Pricing in FinTech Credit: Evidence from P2P Lending</h4>
<p class="pub-meta">
<strong>Authors:</strong> Baals, L.J., Osterrieder, J., Hirsa, A.<br>
<strong>Status:</strong> SSRN Working Paper (2025)<br>
<strong>DOI:</strong> <a href="https://doi.org/10.2139/ssrn.5421207" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.2139/ssrn.5421207</a>
</p>
</div>
</div>

<!-- Appendix B: Open Science Deposits -->
<div class="appendix-section">
<h3>Appendix B: Open Science Deposits (Zenodo)</h3>

<div class="zenodo-grid">
{% for output in site.data.research_outputs %}
<div class="zenodo-card">
<span class="type-badge">{{ output.resource_type }}</span>
<h4>{{ output.title }}</h4>
<p style="font-size: 0.8rem; color: #666; margin: 0.5rem 0;">
{{ output.creators | join: ", " }} ({{ output.publication_date | slice: 0, 4 }})
</p>
<a href="{{ output.zenodo_url }}" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer" style="font-size: 0.8rem;">View on Zenodo</a>
</div>
{% endfor %}
</div>
</div>

<!-- Appendix C: Academic Events -->
<div class="appendix-section">
<h3>Appendix C: Academic Events and Presentations</h3>

<ul class="event-list">
<li>
<span class="date">Dec 2024</span>
<div class="details">
<strong>4th International Symposium on Big Data and AI</strong><br>
<span class="location">Hong Kong - Systematic Literature Review on Graph-Based Credit Models</span>
</div>
</li>
<li>
<span class="date">Sep 2024</span>
<div class="details">
<strong>8th Bern Conference on Fintech and AI in Finance</strong><br>
<span class="location">Bern, Switzerland - Leveraging Network Topology for Credit Risk Assessment</span>
</div>
</li>
<li>
<span class="date">Sep 2024</span>
<div class="details">
<strong>AI Finance Insights: Pioneering the Future of Fintech</strong><br>
<span class="location">ITU, Istanbul, Turkey - Network-Based Prediction of Loan Default Risk</span>
</div>
</li>
<li>
<span class="date">May 2024</span>
<div class="details">
<strong>COST FinAI Meets Istanbul Conference</strong><br>
<span class="location">Istanbul, Turkey - Leveraging Network Topology for Credit Risk Assessment</span>
</div>
</li>
<li>
<span class="date">May 2024</span>
<div class="details">
<strong>Expert Day Workshop</strong><br>
<span class="location">FINMA Campus, Bern, Switzerland - Knowledge Transfer</span>
</div>
</li>
<li>
<span class="date">Dec 2023</span>
<div class="details">
<strong>16th ERCIM Conference on Computational and Methodological Statistics</strong><br>
<span class="location">Berlin, Germany - Leveraging network topology for credit risk assessment</span>
</div>
</li>
<li>
<span class="date">Sep 2023</span>
<div class="details">
<strong>8th European COST Conference on AI in Finance</strong><br>
<span class="location">Bern, Switzerland - Predicting Loan Default in P2P lending</span>
</div>
</li>
<li>
<span class="date">Sep 2023</span>
<div class="details">
<strong>European Summer School in Financial Mathematics</strong><br>
<span class="location">Delft, Netherlands - Poster Presentation</span>
</div>
</li>
</ul>
</div>

<!-- Appendix D: Datasets -->
<div class="appendix-section">
<h3>Appendix D: Datasets</h3>

<div class="pub-item">
<h4>Bondora P2P Lending Dataset</h4>
<p class="pub-meta">
<strong>Repository:</strong> Bondora Public Reports, IEEE DataPort, Kaggle<br>
<strong>Coverage:</strong> June 16, 2009 - April 21, 2022<br>
<strong>Sample Size:</strong> 231,039 individual borrowers<br>
<strong>Features:</strong> 112 categorical and continuous variables<br>
<strong>DOI:</strong> <a href="https://doi.org/10.21227/33kz-0s65" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">10.21227/33kz-0s65</a><br>
<strong>License:</strong> Creative Commons Attribution 4.0
</p>
</div>
</div>

<!-- Appendix E: Additional Funding -->
<div class="appendix-section">
<h3>Appendix E: Additional Funding Secured</h3>

<div class="stats-grid">
<div class="stat-card">
<div class="number">CHF 50k</div>
<div class="label">Leading House Asia (ETH)</div>
</div>
<div class="stat-card">
<div class="number">CHF 20k</div>
<div class="label">SNSF Mobility (Baals)</div>
</div>
<div class="stat-card">
<div class="number">CHF 20k</div>
<div class="label">SNSF Mobility (Liu)</div>
</div>
</div>
</div>

<!-- Appendix F: International Collaborations -->
<div class="appendix-section">
<h3>Appendix F: International Collaborations</h3>

<ul>
<li><strong>Masaryk University</strong> (Czech Republic) - Publications, in-depth exchanges</li>
<li><strong>Columbia University</strong> (USA) - Method exchanges, personnel exchange</li>
<li><strong>American University of Sharjah</strong> (UAE) - Publications, personnel exchange</li>
<li><strong>Renmin University of China</strong> (China) - Method exchanges, publications</li>
<li><strong>University of Manchester</strong> (UK) - Publications</li>
</ul>
</div>

<!-- Appendix G: Research Networks -->
<div class="appendix-section">
<h3>Appendix G: Research Networks</h3>

<ul>
<li><strong>COST Action CA19130 - Fintech and AI in Finance</strong><br>
Role: Action Chair (Joerg Osterrieder)<br>
Website: <a href="https://www.ai-in-finance.eu" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">www.ai-in-finance.eu</a></li>
<li><strong>MSCA Industrial Doctoral Network on Digital Finance</strong><br>
Role: Coordinator (Joerg Osterrieder)<br>
Website: <a href="https://www.digital-finance-msca.com" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">www.digital-finance-msca.com</a></li>
</ul>
</div>

<!-- Appendix H: Knowledge Transfer -->
<div class="appendix-section">
<h3>Appendix H: Knowledge Transfer Events</h3>

<ul class="event-list">
<li>
<span class="date">May 2024</span>
<div class="details">
<strong>Expert Day Workshop</strong><br>
<span class="location">FHNW Campus Brugg-Windisch, Switzerland</span>
</div>
</li>
<li>
<span class="date">Sep 2023</span>
<div class="details">
<strong>International Week, Shenzhen Technology University</strong><br>
<span class="location">Shenzhen, China</span>
</div>
</li>
</ul>
</div>

<!-- Appendix I: Public Communication -->
<div class="appendix-section">
<h3>Appendix I: Public Communication</h3>

<ul>
<li><strong>Shenzhen Technology University - International Week</strong> (2024) - Talks/Events, International</li>
<li><strong>MSCA Digital Finance</strong> (2024) - Webpage, New Media, International</li>
<li><strong>Shenzhen Technology University - International Week</strong> (2023) - Talks/Events, International</li>
</ul>
</div>

<!-- Appendix J: Use-Inspired Outputs -->
<div class="appendix-section">
<h3>Appendix J: Use-Inspired Outputs</h3>

<ul>
<li><strong>REA Expert Reviewer</strong> (2023) - Expert reviewer for the Research Executive Agency under the European Commission's EISMEA programme</li>
<li><strong>EIC Accelerator Expert</strong> (2022) - Expert evaluator for the European Innovation Council Work Programme</li>
</ul>
</div>

<!-- Appendix K: Official Dataset -->
<div class="appendix-section">
<h3>Appendix K: Official Dataset</h3>

<div class="pub-item">
<h4>LoanData - Bondora P2P Lending Dataset</h4>
<p class="pub-meta">
<strong>Curator:</strong> Liu Yiting<br>
<strong>Repository:</strong> Open Science Framework (OSF)<br>
<strong>URL:</strong> <a href="https://osf.io/jnpfs/" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">https://osf.io/jnpfs/</a><br>
<strong>Description:</strong> European P2P lending platform data with loan performance metrics
</p>
</div>
</div>

<!-- Appendix L: PhD Researchers -->
<div class="appendix-section">
<h3>Appendix L: PhD Researcher Details</h3>

<div class="pub-item">
<h4>Lennart John Baals</h4>
<p class="pub-meta">
<strong>Status:</strong> PhD In Progress<br>
<strong>Institution:</strong> Bern University of Applied Sciences / University of Twente<br>
<strong>Research Focus:</strong> Graph-based credit models, network analysis for credit risk assessment<br>
<strong>Publications from Thesis:</strong>
</p>
<ul style="margin-top: 0.5rem; font-size: 0.9rem;">
<li>Liu et al. (2024) Expert Systems with Applications - 17 citations</li>
<li>Liu et al. (2024) Finance Research Letters - 11 citations</li>
<li>Baals et al. (2025) Network Evidence on Credit-Risk Pricing (SSRN)</li>
<li>Baals et al. (2025) State-Dependent Pricing in FinTech Credit (SSRN)</li>
</ul>
</div>

<div class="pub-item">
<h4>Yiting Liu</h4>
<p class="pub-meta">
<strong>Status:</strong> PhD In Progress<br>
<strong>Institution:</strong> Bern University of Applied Sciences / University of Twente<br>
<strong>Research Focus:</strong> P2P lending risk modeling, network topology for credit risk<br>
<strong>Background:</strong> Statistics and quantitative finance from Alliance Manchester Business School and Fudan University<br>
<strong>Publications from Thesis:</strong>
</p>
<ul style="margin-top: 0.5rem; font-size: 0.9rem;">
<li>Liu et al. (2024) Expert Systems with Applications - 17 citations</li>
<li>Liu et al. (2024) Finance Research Letters - 11 citations</li>
</ul>
</div>
</div>

<!-- Appendix M: Data Management Plan -->
<div class="appendix-section">
<h3>Appendix M: Data Management Plan Summary</h3>

<div class="pub-item">
<p class="pub-meta">
This summary addresses the updated Data Management Plan as recommended by <a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF lifetime management best practices</a>.
</p>
</div>

<table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
<tr style="background: var(--gold-light);">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Category</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Status</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Details</th>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Research Data</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Archived</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Bondora dataset on OSF; processed data in Zenodo deposits</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Code/Scripts</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Archived</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Python/R scripts in 12 Zenodo deposits with DOIs</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Documentation</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Complete</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">README files, Jupyter notebooks with inline documentation</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Licensing</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">CC-BY 4.0</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">All outputs freely reusable with attribution</td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><strong>Long-term Access</strong></td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Guaranteed</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Zenodo (CERN), OSF, GitHub (Digital-AI-Finance)</td>
</tr>
</table>
</div>

<!-- Appendix N: SNSF Compliance -->
<div class="appendix-section">
<h3>Appendix N: SNSF Requirements Compliance</h3>

<div class="pub-item">
<p class="pub-meta">
This report complies with SNSF reporting requirements as documented in the following official sources:
</p>
</div>

<table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
<tr style="background: var(--gold-light);">
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Requirement</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Section</th>
<th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Source</th>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Achievement of Objectives</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">1.1 (Mandatory)</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Lifetime Management</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Challenges & Negative Results</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">1.2</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Lifetime Management</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Knowledge Advancement</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">1.3</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Lifetime Management</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Impact Statement</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Extended: 1.4</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/eBcE6xqoFI2PAqhI/page/funding/regulations-whats-new" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF 2025 Best Practices</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Sustainability Plan</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Extended: 1.5</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/eBcE6xqoFI2PAqhI/page/funding/regulations-whats-new" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF 2025 Best Practices</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Output Data</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Appendices A-K</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/Z2GsZbMCeccg4x9U/page/funding/documents-downloads" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Documents & Downloads</a></td>
</tr>
<tr>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Data Management Plan</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;">Appendix M</td>
<td style="padding: 0.75rem; border: 1px solid #ddd;"><a href="https://www.snf.ch/en/O5R5SHXroj5b4ulK/page/funding/how-to/lifetime-management-of-projects" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Lifetime Management</a></td>
</tr>
</table>
</div>

</div>
</details>

<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: var(--gold-light); border-radius: 8px;">
<p style="margin: 0; color: var(--navy);">
<strong>Report submitted to:</strong> Swiss National Science Foundation (SNSF)<br>
<strong>Report date:</strong> December 2025<br>
<strong>Data source:</strong> <a href="https://data.snf.ch/grants/grant/205487" target="_blank" rel="noopener noreferrer" referrerpolicy="no-referrer">SNSF Data Portal - Grant 205487</a>
</p>
</div>

</div>
