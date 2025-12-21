---
layout: default
title: Final Scientific Report
permalink: /final-report/
description: SNSF Final Scientific Report for Project 205487 - Network-Based Credit Risk Models in P2P Lending Markets
---

<style>
.report-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
  line-height: 1.8;
}
.report-container h1 {
  text-align: center;
  margin-bottom: 0.5rem;
}
.report-container .subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 2rem;
}
.report-container h2 {
  margin-top: 2.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--gold);
}
.report-container h3 {
  margin-top: 1.5rem;
}
.report-container h4 {
  margin-top: 1.2rem;
  margin-bottom: 0.5rem;
}
.meta-table {
  margin: 1rem auto 2rem;
  border-collapse: collapse;
}
.meta-table td {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
}
.meta-table td:first-child {
  font-weight: 600;
}
.extended-info {
  margin-top: 3rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.extended-info summary {
  padding: 1rem;
  cursor: pointer;
  font-weight: 600;
  background: #f5f5f5;
}
.extended-info .extended-content {
  padding: 1.5rem;
}
</style>

<div class="report-container">

<h1>Final Scientific Report</h1>
<p class="subtitle">Network-Based Credit Risk Models in P2P Lending Markets</p>

<table class="meta-table">
<tr>
<td>Name</td>
<td>Prof. Dr. Joerg Osterrieder</td>
</tr>
<tr>
<td>Project number</td>
<td>205487</td>
</tr>
</table>

<h2>1.1 Achievement of research objectives (mandatory)</h2>

<p><strong>Main Objective:</strong> To advance our understanding of credit risk modeling in P2P lending markets by designing and empirically verifying new network-based credit risk models. This project has attributes of a methodological and empirical project with practical impact, addressing information asymmetry inherent in P2P lending through network analysis.</p>

<h4>Contribution 1 (Methodological): Supervised Network-Based Credit Risk Models</h4>

<p>Previous methods (Ahelegbey et al., 2019; Giudici et al., 2019, 2020) ignored loan status, leading to unsupervised network-based learning. Our approach utilizes class information (loan default status) to construct supervised networks, as supervised learning generally outperforms unsupervised approaches. We developed a two-step machine learning methodology that constructs borrower similarity graphs and extracts multiple centrality measures (PageRank, betweenness, closeness, Katz, hub/authority) as predictive features.</p>

<p><strong>Evidence:</strong> Liu et al. (2024), "Leveraging network topology for credit risk assessment in P2P lending," <em>Expert Systems with Applications</em>, Vol. 252, Article 124100. 17 citations.</p>

<h4>Contribution 2 (Methodological): Cross-Validation for Network Hyperparameters</h4>

<p>In contrast to previous studies, our work acknowledges that network creation and feature extraction depend on hyperparameters. We applied cross-validation to tune network hyperparameters and resulting features, including similarity thresholds, k-nearest-neighbor connection rules, and centrality measure configurations. This systematic approach to hyperparameter optimization contrasts with prior work that used fixed, ad-hoc parameter choices.</p>

<p><strong>Evidence:</strong> Methods sections in Liu et al. (2024) ESWA and FRL publications; hyperparameter sensitivity analysis in Zenodo deposits.</p>

<h4>Contribution 3 (Methodological): Multiple Networks with Bootstrap Aggregation</h4>

<p>Previous studies created only one network. We designed methods to create multiple networks that: (i) utilize different (random) sets of variables, and (ii) rely on bootstrap aggregation (bagging). This directly addresses data noisiness, which is ignored in existing literature. The approach was validated using Elastic Net, Random Forest, Multi-Layer Perceptron, and XGBoost ensemble methods.</p>

<p><strong>Evidence:</strong> Ensemble methodology in publications; robustness checks using shuffled centrality features confirmed predictive value.</p>

<h4>Contribution 4 (Empirical): Validation Across Multiple P2P Datasets</h4>

<p>We enriched the empirical literature (most studies use fewer than two datasets) by validating models across different market platforms. Primary analysis used the Bondora dataset (231,039 borrowers, 112 variables, European P2P market), with comparative validation using LendingClub data (US market). This enabled observation of credit drivers across platforms with different geographic and regulatory characteristics.</p>

<p><strong>Evidence:</strong> Liu et al. (2024), "Network centrality and credit risk," <em>Finance Research Letters</em>, Vol. 63, Article 105308. 11 citations.</p>

<h4>Contribution 5 (Practical): Explainable AI for Interpretable Credit Risk Models</h4>

<p>We investigated the applicability of XAI methods (SHAP, LIME) to credit scoring models, enabling estimation of both global effects (expected effect of each variable on outcome) and local effects (expected effect of each variable for a specific individual loan). This addresses regulatory requirements for interpretable automated lending decisions (GDPR, policymaker trends). Surrogate decision trees and manual tree-based interpretation frameworks were developed for regime detection models.</p>

<p><strong>Evidence:</strong> SHAP explainability notebooks in Zenodo deposit 17991107; tree-based interpretation framework in Zenodo deposit 17990398; 12 Zenodo deposits ensuring reproducibility.</p>

<h3>Additional Project Outcomes</h3>

<h4>Research Capacity Building and International Collaboration</h4>

<p>The project trained two PhD researchers (Lennart John Baals and Yiting Liu) who developed expertise in digital finance, network modeling, and explainable AI. We established collaborations with five international institutions across four continents (Masaryk University, Columbia University, American University of Sharjah, Renmin University of China, University of Manchester). The PI serves as Action Chair of COST Action CA19130 (Fintech and AI in Finance) and Coordinator of the MSCA Industrial Doctoral Network on Digital Finance.</p>

<p><strong>Additional Funding Secured:</strong> The project's success attracted CHF 90,000 in additional funding: two SNSF Mobility Grants (CHF 20,000 each) and a Leading House Asia grant (CHF 50,000) for related digital assets research.</p>

<h2>1.2 Challenges, negative results and unexpected outcomes</h2>

<p><strong>Data Access Challenges:</strong> The original proposal planned validation across 7 P2P platforms (Lending Club, Prosper, Zopa, Mintos, Bondora, Home Credit, Kiva). Due to data access restrictions, platform terms of service (e.g., Bondora section 13.4 preventing redistribution), and proprietary data policies, we focused primary empirical analysis on Bondora (European) with comparative validation using LendingClub (US), providing geographic and regulatory diversity. This led us to focus on reproducible code and documentation in our Zenodo deposits.</p>

<p><strong>Platform Evolution:</strong> The P2P lending landscape evolved significantly during the project period, with some platforms reducing operations or changing data policies. Several planned data sources became unavailable or restricted. This required flexibility in our empirical strategy, ultimately strengthening our focus on methodological contributions applicable across different platforms.</p>

<p><strong>Computational Scaling:</strong> Network construction for large loan portfolios presented computational challenges. We addressed this through efficient similarity thresholding and k-nearest-neighbor connection rules to maintain connectivity while managing graph size.</p>

<p><strong>Unexpected Finding:</strong> Our analysis revealed that network position (degree centrality) alone provides substantial predictive power, sometimes matching or exceeding more complex centrality measures. This simplified insight has practical implications for platform operators seeking interpretable risk indicators.</p>

<h2>1.3 Contribution to knowledge advancement</h2>

<p><strong>Methodological Contribution:</strong> We established network topology as a viable and valuable feature source for credit risk modeling in P2P lending. Our two-step ML approach provides a replicable framework for combining structural and attribute-based predictors. The systematic literature review (78 articles analyzed) provides a comprehensive synthesis of graph-based credit modeling approaches.</p>

<p><strong>Practical Impact:</strong> Our models and code are directly applicable to P2P lending platforms for risk assessment. The interpretability framework using SHAP/LIME enables platform operators to explain credit decisions to borrowers and regulators, addressing transparency requirements in automated lending decisions.</p>

<p><strong>Open Science Contribution:</strong> All 12 Zenodo deposits (100% open access) ensure complete reproducibility of our findings. The deposits include LaTeX sources, Jupyter notebooks, Python/R scripts, and comprehensive documentation, enabling other researchers to validate, extend, and build upon our work.</p>

<p><strong>Capacity Building:</strong> Two PhD researchers were trained in cutting-edge methods at the intersection of network science, machine learning, and finance. Knowledge transfer activities included an Open Day workshop at FINMA (Swiss financial regulator) and presentations at international research events in eight countries.</p>

<p><strong>Research Network Leadership:</strong> The PI's roles as COST Action Chair and MSCA Network Coordinator enabled broad dissemination of project findings across 40+ European institutions, creating lasting infrastructure for fintech research collaboration.</p>

<details class="extended-info">
<summary>Extended Project Information</summary>
<div class="extended-content">

<h3>Project Statistics</h3>
<ul>
<li>6+ Core Publications</li>
<li>28+ Citations Received</li>
<li>12 Zenodo Deposits</li>
<li>8 Conference Presentations</li>
<li>2 PhD Researchers Trained</li>
<li>CHF 90k Additional Funding</li>
</ul>

<h3>Executive Summary</h3>

<p>This Final Scientific Report documents the successful completion of SNSF Project 205487 "Network-Based Credit Risk Models in P2P Lending Markets" (October 2022 - August 2025). The project achieved all its research objectives, producing significant methodological innovations and empirical contributions to the field of digital finance.</p>

<h3>1.4 Impact Statement</h3>

<p><strong>Scientific Impact:</strong> Our publications have received 28+ citations within 12 months of publication, indicating rapid adoption by the research community. The two-step ML methodology combining network centrality with traditional credit features has been referenced in subsequent studies on P2P lending risk assessment.</p>

<p><strong>Economic Impact:</strong> The developed models and open-source code are directly applicable to P2P lending platforms for improved credit risk assessment. By enabling more accurate default prediction, platforms can better price loans, reduce losses, and offer more competitive rates to creditworthy borrowers.</p>

<p><strong>Social Impact:</strong> Improved credit risk models contribute to financial inclusion by enabling P2P platforms to serve borrowers who may be underserved by traditional banking. Better risk assessment reduces adverse selection, protecting retail investors who fund P2P loans.</p>

<p><strong>Policy Impact:</strong> The project engaged directly with financial regulators through the Open Day workshop (May 2024), presenting research findings to Swiss financial supervisory staff. The PI's leadership of COST Action CA19130 facilitated policy discussions at EU level.</p>

<p><strong>Educational Impact:</strong> The project trained 2 PhD researchers in cutting-edge methods at the intersection of network science, machine learning, and finance. The publication "Towards a new PhD Curriculum for Digital Finance" (Open Research Europe, 2024) disseminates best practices for doctoral training in this emerging field.</p>

<h3>1.5 Sustainability Plan</h3>

<p><strong>Data Preservation:</strong> 12 Zenodo deposits archived with DOIs ensuring permanent accessibility and citability. Curated dataset (Bondora P2P Lending) archived at OSF. Code repositories maintained under Digital-AI-Finance organization on GitHub. All outputs under Creative Commons Attribution 4.0 (CC-BY 4.0).</p>

<p><strong>Code Maintainability:</strong> All Jupyter notebooks and Python scripts include dependency specifications (requirements.txt). Reproducibility verified through independent testing. Documentation embedded in code and supplementary README files.</p>

<p><strong>Knowledge Transfer Continuation:</strong> COST Action CA19130 (Fintech and AI in Finance) continues beyond project end. MSCA Digital Finance Network continues training next-generation researchers. Digital finance research continues at Bern University of Applied Sciences.</p>

<h3>Appendix A: Peer-Reviewed Publications</h3>

<p><strong>Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B.</strong> (2024). Leveraging network topology for credit risk assessment in P2P lending: A comparative study under the lens of machine learning. <em>Expert Systems with Applications</em>, 252(B), 124100. DOI: 10.1016/j.eswa.2024.124100. 17 citations.</p>

<p><strong>Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B.</strong> (2024). Network centrality and credit risk: A comprehensive analysis of peer-to-peer lending dynamics. <em>Finance Research Letters</em>, 63, 105308. DOI: 10.1016/j.frl.2024.105308. 11 citations.</p>

<p><strong>Baumohl, E., Lyocsa, S., Vasanicova, P.</strong> (2024). Macroeconomic environment and the future performance of loans: Evidence from three peer-to-peer platforms. <em>International Review of Financial Analysis</em>, 95, 103416. DOI: 10.1016/j.irfa.2024.103416.</p>

<p><strong>Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Liu, Y.</strong> (2024). Towards a new PhD Curriculum for Digital Finance. <em>Open Research Europe</em>, 4, 16513. DOI: 10.12688/openreseurope.16513.1.</p>

<p><strong>Submitted / Under Review:</strong></p>

<p><strong>Baals, L.J., Osterrieder, J., Hadji-Misheva, B., Gomez, L., Wang, Y.</strong> (2025). Network Evidence on Credit-Risk Pricing in P2P Lending. SSRN Working Paper. DOI: 10.2139/ssrn.5276337.</p>

<p><strong>Baals, L.J., Osterrieder, J., Hirsa, A.</strong> (2025). State-Dependent Pricing in FinTech Credit: Evidence from P2P Lending. SSRN Working Paper. DOI: 10.2139/ssrn.5421207.</p>

<h3>Appendix B: Open Science Deposits (Zenodo)</h3>

{% for output in site.data.research_outputs %}
<p><strong>{{ output.title }}</strong><br>
{{ output.creators | join: ", " }} ({{ output.publication_date | slice: 0, 4 }}). {{ output.resource_type }}. <a href="{{ output.zenodo_url }}" target="_blank" rel="noopener noreferrer">View on Zenodo</a></p>
{% endfor %}

<h3>Appendix C: Academic Events and Presentations</h3>

<ul>
<li>Dec 2024: 4th International Symposium on Big Data and AI, Hong Kong</li>
<li>Sep 2024: 8th Bern Conference on Fintech and AI in Finance, Switzerland</li>
<li>Sep 2024: AI Finance Insights: Pioneering the Future of Fintech, Istanbul</li>
<li>May 2024: COST FinAI Meets Istanbul Conference, Turkey</li>
<li>May 2024: Open Day Workshop, FINMA Campus, Bern</li>
<li>Dec 2023: 16th ERCIM Conference on Computational and Methodological Statistics, Berlin</li>
<li>Sep 2023: 8th European COST Conference on AI in Finance, Bern</li>
<li>Sep 2023: European Summer School in Financial Mathematics, Delft</li>
</ul>

<h3>Appendix D: Datasets</h3>

<p><strong>Bondora P2P Lending Dataset</strong><br>
Repository: Bondora Public Reports, IEEE DataPort, Kaggle<br>
Coverage: June 16, 2009 - April 21, 2022<br>
Sample Size: 231,039 individual borrowers<br>
Features: 112 categorical and continuous variables<br>
DOI: 10.21227/33kz-0s65<br>
License: Creative Commons Attribution 4.0</p>

<h3>Appendix E: International Collaborations</h3>

<ul>
<li>Masaryk University (Czech Republic) - Publications, in-depth exchanges</li>
<li>Columbia University (USA) - Method exchanges, personnel exchange</li>
<li>American University of Sharjah (UAE) - Publications, personnel exchange</li>
<li>Renmin University of China (China) - Method exchanges, publications</li>
<li>University of Manchester (UK) - Publications</li>
</ul>

<h3>Appendix F: Research Networks</h3>

<ul>
<li>COST Action CA19130 - Fintech and AI in Finance (Role: Action Chair)</li>
<li>MSCA Industrial Doctoral Network on Digital Finance (Role: Coordinator)</li>
</ul>

<h3>Appendix G: PhD Researcher Details</h3>

<p><strong>Lennart John Baals</strong><br>
Status: PhD In Progress<br>
Institution: Bern University of Applied Sciences / University of Twente<br>
Research Focus: Graph-based credit models, network analysis for credit risk assessment</p>

<p><strong>Yiting Liu</strong><br>
Status: PhD In Progress<br>
Institution: Bern University of Applied Sciences / University of Twente<br>
Research Focus: P2P lending risk modeling, network topology for credit risk</p>

</div>
</details>

<p style="text-align: center; margin-top: 3rem; padding: 1.5rem; background: #f5f5f5; border-radius: 4px;">
<strong>Report submitted to:</strong> Swiss National Science Foundation (SNSF)<br>
<strong>Report date:</strong> December 2025<br>
<strong>Data source:</strong> <a href="https://data.snf.ch/grants/grant/205487" target="_blank" rel="noopener noreferrer">SNSF Data Portal - Grant 205487</a>
</p>

</div>
