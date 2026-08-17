# DPI Public Value Framework

**Theoretical foundation for policy analysis of digital public infrastructure**

Derived from:
- Mazzucato, M., Eaves, D. and Vasconcellos, B. (2024). *Digital public infrastructure and public value: What is 'public' about DPI?* UCL IIPP Working Paper 2024-05. — hereafter **[MEV24]**
- Eaves, D., Coyle, D., Vasconcellos, B. and Deshmukh, S. (2025). *The Economics of Shared Digital Infrastructures: A framework for assessing societal value.* IIPP Policy Report 2025/02. — hereafter **[ECVD25]**

---

## 0. How to use this framework

This is an **analytical instrument**, not a literature summary. Each module below is a gate: it defines what to look for in the policy object, what inference to draw, and what conclusion is not permitted on the available evidence.

**Standing order.** Run modules in sequence. A policy object that fails Module 1 is not DPI and the remaining modules do not apply to it as infrastructure. Do not skip Module 3 (governance) to reach a verdict from Modules 2 and 4 alone — the central claim of [MEV24] is that technical attributes and stated functions are jointly insufficient to establish publicness.

**Unit of analysis.** A specific digital system, or a specific policy/investment/governance decision about one. Not "digital transformation" in general.

**Default posture.** Sceptical but not dismissive. The papers argue DPI has substantial value-creation potential *and* that the potential is not self-executing. Both halves are load-bearing. An analysis that concludes only "this will deliver inclusive growth" or only "this will entrench monopoly" has almost certainly skipped a module.

---

## 1. Threshold test — is this actually infrastructure?

**Purpose.** Prevent the most common category error: treating any government IT project, digitised service, or platform as DPI. [ECVD25] is explicit that DPI is defined by a *systemic approach*, not by membership of a component list.

### 1.1 Frischmann's three criteria [MEV24, §2.1, after Frischmann 2012]

Infrastructure is a **"shared means to many ends"**. The resource must:

1. Be **consumed non-rivalrously** for an appreciable range of demand;
2. Have social demand driven **primarily by downstream productive activities** that use it as an input;
3. Be usable as an input into a **wide range** of goods and services — private, public and social.

Criterion 1 admits impure public goods: if the digital system relies on limited storage or processing power, congestion makes it impure, not disqualified. Criterion 2 is the discriminating one in practice — a system whose demand is *terminal* (people want the service itself) is a service, not infrastructure.

### 1.2 The eight infrastructural characteristics [ECVD25, §2.1, expanding Frischmann]

| # | Characteristic | Grouping |
|---|---|---|
| 1 | Essential input to a range of activities (market participation or basic societal needs) | Relevance |
| 2 | Long-lived collective asset; high upfront cost relative to low marginal cost of supply | Financing |
| 3 | Non-rival up to congestion limits | Financing |
| 4 | Collective and non-excludable (access universal or not dependent on personal relationships/identity) | Financing |
| 5 | Generic or standardised capital services, usable as inputs to a wide range of activities | Financing |
| 6 | Derived demand — value created by downstream applications | Dynamic |
| 7 | Creates spillovers and externalities | Dynamic |
| 8 | Complements or substitutes for other infrastructures | Nature |

**Analytical move.** Score the object 1–8 as *present / limited / absent*. [ECVD25, Table 1] positions siloed digitalisation as "limited" on characteristics 1–4 and "no" on 5–8. **Characteristics 5–8 are the discriminator**: a system that is merely a better-built service will show limited relevance and financing properties but will not exhibit generic capital services, derived demand, spillovers or layering.

Characteristic 1 anchors the conversation in a **rights-based or state-capacity discourse rather than an economic one** — note when a document leans on this, because it changes what evidence is owed. Characteristics 2–5 explain why *government funding or coordination* is implicated: non-rivalry creates a classic free-rider problem; universal access implies cross-subsidy from profitable to non-profitable users; the long-lived character requires an investor with a sufficiently low discount or hurdle rate. Characteristics 6–8 are why returns are **hard to identify empirically** — the academic literature has failed to find consistently positive returns to infrastructure investment even though no economy functions without it.

### 1.3 Stack placement [MEV24, Figure 1]

Locate the object in the three-layer stack:

- **Services** (renew a passport, apply for benefits, buy products)
- **Shared infrastructure** (ID systems, payment systems, data exchange layers, emerging sectoral layers) ← *DPI sits here*
- **Data and hardware** (health records, civil registries, geospatial data)

Upper layers leverage resources created below. Misplacement is diagnostic: a document that promises infrastructural returns from a service-layer investment has an unfunded logical step.

### 1.4 Note on the definitional boundary

[ECVD25] takes the broad approach: *all digital systems with public infrastructural characteristics* count, not only the canonical triad (digital ID/authentication, secure data exchange, real-time payments). Use the broad definition, but state which you are using — the narrow triad reading changes what counts as in-scope.

**Do not conclude** that a system is DPI because it is publicly owned, because it is regulated, or because its operator claims public benefit. [MEV24, §4] shows this test admits Mastercard, Visa and American Express, which is why it is inadequate.

---

## 2. Publicness audit — surface the implicit normative claim

**Purpose.** [MEV24]'s core contribution: "public" in DPI is never neutral. Every organisation in the DPI space has an *implicit interpretation of public interest with normative values embedded in it*. The analyst's first job is to make the implicit explicit.

### 2.1 The three rungs of 'P' [MEV24, Figure 4]

| Rung | Content | Diagnostic |
|---|---|---|
| **Public interest** | An ideal to be pursued, but vague and not tied to specific content (Bozeman 2002, 2007) | Produces confusing DPI definitions; cannot adjudicate between competing systems |
| **Public values** | Have content; can be identified, measured, evaluated. Provide normative consensus about (a) rights/benefits/prerogatives citizens should be entitled to, (b) obligations of citizens to society, the state and one another, (c) principles on which government and policy should be based (Bozeman 2007) | *What is actually happening in practice, whether or not it is stated* |
| **Public value maximisation** | Explicit public values + governance following the five common-good pillars + proactive, market-shaping state | The paper's proposed interpretation |

**Analytical move.** Identify which rung the document operates on. If it invokes "public interest" without content, name that as a finding, not a neutral description — it is precisely the move that lets any regulated private infrastructure claim the label.

### 2.2 The attributes/functions grid [MEV24, Table 2]

Every publicness claim in the DPI literature reduces to one of seven arguments. Classify each claim in the document:

**Attributes framing** — value from technical properties; implicit values are *dynamic efficiency and scale*:

| Claim | Mechanism |
|---|---|
| Interoperable through open standards | Prevents lock-in; improves and shapes competition; converts "shared means to many ends" into *universally* shared means |
| Built from reusable building blocks | Higher network effects and combinatorial innovation; modular subcomponents (unlike analogue infrastructure, which is technically indivisible) |
| Open-source licensed / unlicensed / public domain | Positive externalities via adoptability, adaptability, prevention of lock-in |

**Functions framing** — value from societal purposes achieved; implicit values are more directly normative:

| Claim | Implicit value | Mechanism |
|---|---|---|
| Fosters community and social relationships | Social value | Inter- and intra-communal relationships (Zuckerman 2020: infrastructures that let us engage in public and civic life in digital spaces) |
| Fosters economic activity | Economic value | Financial inclusion; mobilising the potentialities of economic agents (Buhr 2003) |
| Guarantees essential capabilities | Capabilities and human rights | Sen's capability approach; Eaves and Sandman (2023): society-wide digital capabilities essential to participation in society and markets as citizen, entrepreneur and consumer |
| Guarantees better quality of life | Essential needs and human rights | Essential human needs (Buhr 2003); right to legal identity (SDG 16.9) |

### 2.3 The two-sided critique [MEV24, §4.2]

This is the analytically productive part. Apply both blades:

**Against attributes alone:** the framing is **broadly agnostic on the direction of outcomes**. It assumes innovation from the infrastructure will create positive spillovers in unspecified markets and formats. Downside: *DPI investment and implementation effort wasted in areas that are not policy-relevant or priority.*

**Against functions alone:** a system built with a specific function but non-compliant with attributes **wastes the opportunity for societal impact and is less resilient to political shifts**. Features are complicated to change over time, whereas an ill-intentioned leader can reshuffle governance more easily — which is exactly why attributes matter for the *sustainability and endurance* of public values.

**Against both:** neither accounts for the **processes** surrounding value creation and maximisation, or the political economy implications. *Nothing intrinsic about the attributes or functions of DPI creates inclusion, transparency and trust.* And both are broadly silent on the **state's role**, defaulting to a market-failure framing that is "not helpful".

**Analytical move.** For each document, state: which framing dominates; what the framing is silent on; and what the silence permits. A combined attributes+functions position is desirable but still insufficient — it must be carried into Module 3.

---

## 3. Common-good governance test

**Purpose.** [MEV24, §5] — public value *creation* is not public value *maximisation*. Creation asks how society benefits from value created; maximisation asks about the **process**: its direction, how it happens, who is involved, and who guarantees it — more than who runs it.

The common good "is not a correction, but a bold objective reached collectively" (Mazzucato 2023), in contrast to market-failure theory which is "more about corrections than objectives". The philosophical principle extends beyond attaining common objectives to foreground **the common processes and relationships needed to achieve them** — the 'how' of the journey is as crucial as the destination. Applied to economics, it moves beyond maximising individual preferences and Pareto efficiency as the ultimate goal.

### 3.1 The architecture [MEV24, Figure 3b]

```
                    Common Good Outcomes
                            ▲
                    Public Governance
        (the five pillars operating as governance practice)
                            ▲
                      Public Values
   (functional purposes)          (technical attributes)
   essential capabilities          interoperability
   social value                    reusability
   economic value                  open-source software
   quality of life
```

Three things are required, in order: (1) well-defined public values embedded in attributes and functional purposes; (2) the five pillars translated into governance practices and processes; (3) governance and values aligned with clearly articulated, aspirational societal goals.

### 3.2 The five pillars, as diagnostic questions [MEV24, §5.3–5.7]

**Pillar 1 — Purpose and directionality.** Setting an ambitious direction around which policies are designed, public-private partnerships formed and citizens engaged.
- What normative public values support the DPI's creation?
- Is the DPI built considering priority use cases, without losing sight of broader applicability?
- Are civil society organisations and other societal representatives involved in defining purpose?
- Is government responsible for orchestrating design and implementation?

> *Calibration.* India's Aadhaar had explicit directionality — simplify distribution of welfare benefits and reduce leakage — which made additional scaling easier and produced the long tail of KYC uses. Jamaica's digital ID was not built with an explicit primary purpose, which allowed others to imagine the ID's purpose, fostered civil society distrust of government intentions, and wasted the opportunity. The highway analogy: highways were built for rapid redeployment of military equipment; that direction shaped the far larger civilian long tail. **Direction exists whether or not it is chosen.**

**Pillar 2 — Co-creation and participation.** Rules and mechanisms for co-investment, collaboration and coordination across a diverse group of societal actors. Note: this is *parallel to* purpose and directionality, **not a subsequent step**. The legacy of failing to co-create traditional infrastructure — highways created by expropriating land from the most vulnerable, often to serve wealthier communities — is why.
- Are explicit public values driving key design and governance decisions?
- Is there a process for gathering and meaningfully integrating diverse societal perspectives?
- Is the DPI publicly funded or co-funded?

> *Calibration.* Brazil's Pix Forum: 130+ members including credit card operators, banks, fintechs, civil society organisations and small business associations. Processing feedback from 100+ participants made the process harder; the team considers it central to its success. Co-creation around **proprietary** technology, where a commercial company rather than government holds rights, is substantially harder than around open-source or a digital public good.

**Pillar 3 — Collective learning and knowledge-sharing.** Institutional practices supporting collective learning and long-term capabilities. When the state outsources functions it loses institutional memory and implementation capacity.
- Are there processes for documenting learning?
- Are learnings publicly shared?
- Is the code base available for others to reuse?

> *Calibration.* Bangladesh's a2i as a think tank inside government. MOSIP's graded contribution model — some components closely governed to protect safety and do-no-harm mechanisms, others open to external contribution across requirements, design, coding, testing and documentation.

**Pillar 4 — Access for all and reward-sharing.** Public value distributed equitably. If infrastructure is directed towards collective benefits it must be universally accessible and its rewards shared with society — "two ideas not always aligned with private interests".
- Is there a proactive effort to make the DPI universally accessible?
- Are there governance clauses regulating data for the public interest?
- Are the benefits of data use being socialised?
- Are the costs for using the infrastructure low or none?

> *Calibration.* Universal access in the digital domain **unequivocally implies ensuring access through analogue means** — except in the seven countries with near-universal internet use, waiting for universal internet access imposes a burden on citizens. Bangladesh's 9,000+ union digital centres (the "phygital" access layer, within ~4km of any individual). Togo's Novissi reached the most vulnerable through post office agencies and radio partnerships. Barcelona's "new data deal" used **procurement rules** as a public-interest instrument, with data sovereignty clauses asserting the city's mandate over data collected through or about public services.

**Pillar 5 — Transparency and accountability.** Winning and retaining citizens' trust. DPI's **decentralised architecture poses accountability challenges** across departments and levels of government sharing the same infrastructure — unlike monolithic organisations where accountability is vertical and hierarchical. But integration also generates digital footprints that can be leveraged for transparency.
- Can citizens and companies consent to or audit how and when their data is used?
- Are key technical and management decisions available in accessible language and format?
- Is the DPI governed by a public-interest entity?

> *Calibration.* Estonia's e-health portal lets citizens see who accessed their data and when. **Transparency alone does not guarantee accountability or trust** — if data is made available in a way that is not user-friendly, the effect on trust can be neutral or negative.

**The pillars are not to be assessed in isolation.** A DPI strong on transparency and weak on directionality is not "partially common-good"; the framework is combinatorial.

### 3.3 The state's role

Central to the common good is the state as **market shaper and entrepreneur** — not only regulator, but investor or co-investor of first resort, capable of influencing the *quality* of market outcomes. This requires vision and real technology- and sector-specific expertise, not just bureaucratic skill. Thinking of the state as *levelling* the playing field rather than *tilting* it has reduced its confidence in its own capabilities and made it more vulnerable to capture by vested interests.

The **sovereignty argument**: unless the state engages in building DPI, essential societal functions become the exclusive (knowledge) property of private corporations, usually foreign ones. This does not imply government should run and operationalise all DPI components, but that there must be **a minimum mass of implementation capacity to make regulatory approaches meaningful**.

**Analytical move.** Where a document assigns the state a purely regulatory or market-failure-fixing role, flag it: [MEV24] treats this as a category error about what DPI requires, not a legitimate alternative position.

---

## 4. Design characteristics — mechanism and failure mode

**Purpose.** [ECVD25, §3] maps design choices to economic mechanisms. Value is *not automatic*; it depends on technical choices, governance, procurement and financing models. For each characteristic present in the object, trace the mechanism *and* the corresponding risk.

### 4.1 Standardisation
Common rules, formats and protocols creating consistency across systems and processes.

**Mechanisms:** reduces transaction and compliance costs by simplifying integration and regulatory requirements; prevents vendor lock-in by lowering switching costs (*only if the standard is not proprietary*); affects market participation — may enable more of it by lowering entry barriers, or discourage new entrants if standards favour dominant players. A sometimes-overlooked benefit: **commodifying components of an ecosystem**, reducing costs and enabling entirely new industries.

**Risks:** premature or rigid standards lock in specific technologies before markets develop (Kerber et al. 2017); dominant firms shape standards to reinforce market power (Farrell and Klemperer 2007); poorly coordinated standardisation *causes* fragmentation — the EU's eIDAS framework, where national variations in digital identity implementation hindered cross-border use; standardisation without strong governance still produces silos.

**Policy responses:** ensure foundational standards enable cross-sector and cross-border reuse; adopt **minimalist** standards that commodify generic and widely used activities; prioritise public-interest governance in standard-setting.

### 4.2 Interoperability beyond immediate applications
Different systems and organisations exchanging and using data, **including in sectors beyond the original design**.

**Distinction from standardisation:** standardisation defines common rules and formats; interoperability is about how systems *function and interact*. Standardised protocols may exist, but without effective implementation, enforcement and governance, interoperability is not achieved. Treat any document that conflates the two as making an unsupported leap.

**Mechanisms:** breaks down information silos and reduces information asymmetries; minimises redundant IT spending; facilitates spillovers and combinatorial innovation by letting firms build on common layers without direct coordination; shapes market competition — can encourage cross-sector business models, or entrench monopolies if standards or data flows are controlled by dominant players.

**Risks:** privacy vulnerabilities; reinforcement of monopolies or existing inequalities; without regulatory oversight, dominant players influence technical or operational standards to entrench market power (Russell 2014); security risks in sensitive areas such as health data-sharing.

**Policy responses:** regulatory oversight preventing dominant firms from controlling access to shared layers; privacy and security safeguards embedded in cross-sector exchanges; ecosystem-building for cross-sector adoption.

### 4.3 Minimal and reusable building blocks
Modular components repurposed across multiple services.

**The four defining features** [MEV24, §4.1.1, after DPGA GovStack / CGD] — a microservices architecture:
1. **Autonomous** — standalone reusable service or set of services, possibly composed of many modules
2. **Generic** — flexible across use cases and sectors
3. **Interoperable** — able to combine, connect and interact with other building blocks
4. **Iteratively evolvable** — improvable even while in use as part of solutions

**Mechanisms:** reduces redundant infrastructure costs; supports rapid scaling and cross-sector expansion; lowers the cost of innovation by shortening development cycles and enabling customisability without full redesign; enhances long-term sustainability and resilience through targeted upgrades instead of full system overhauls. Combinatorial innovation: "coming up with something new and valuable not by starting from scratch, but instead by putting together in new ways things that were already there" (McAfee and Brynjolfsson 2017).

**Risks:** vendor lock-in where dominant providers control key components, limiting competition and public-sector bargaining power; **fragmentation** where different agencies or jurisdictions build similar components without interoperability, negating the efficiency gain; security concentration — widely used building blocks become attractive targets.

**Policy responses:** modular components adhering to open or common standards; public-sector control or oversight of critical reusable components; security-by-design.

> *Calibration.* GOV.UK Notify: 1,600+ organisations and 10,000+ services as of March 2025. India's Sunbird/Anuvaad: a translation module for Indic languages plugged into both the National Education Platform (Diksha) and SUVAS, the Supreme Court's document translation system.

### 4.4 Data as a high-value input
Data functioning as both an **enabler of more efficient services (input) and an economic and governance asset (output)** — one of the key factors distinguishing DPI from traditional infrastructure.

**Mechanisms (conditional on the data being reliable and well-governed):** reduces information asymmetry and incomplete-data gaps; minimises risk and uncertainty across finance and public services via identity verification, eligibility assessment, cybersecurity and fraud detection; enhances efficiency and targeting, reducing administrative burdens and leakages; supports economic forecasting, AI-driven analytics and crisis response; may strengthen public accountability by enabling transparency in digital transactions and limiting data monopolisation.

**Risks:** the **'spectrum of visibility'** problem — if individuals are 'invisible' in a dataset, compounding effects follow across social protection, transport and finance. Singh and Jackson (2021): rights and entitlements of "high-resolution citizens" are expanded while those of "low-resolution citizens" are curtailed. Poor data quality also weakens the *economic* potential of data as an input: unreliable datasets cannot support AI-driven services, predictive analytics or automated decision-making. Note the **algorithmic imprint** — effects that persist even after algorithms are deemed inappropriate and removed (Ehsan et al. 2022).

**Policy responses:** mechanisms improving data accuracy and universality so underserved populations are not made invisible; interoperable, structured formats; ensuring publicly funded data systems create public benefits rather than reinforcing corporate dominance. Treat data quality as a **core policy priority, not an afterthought** — continuous validation, strong correction mechanisms, clear accountability structures.

### 4.5 Public oversight and governance
Regulatory frameworks, open standards and public-private coordination ensuring DPI operates in the public interest.

**Mechanisms:** creates fair market conditions by preventing monopolisation, excessive rent extraction and anti-competitive practices; keeps DPI a public good by fostering universal adoption, inclusion and trust while maintaining affordability; protects rights and security through data privacy, cybersecurity and ethical data-use regulation.

**Why the economics make governance non-optional:** non-rivalry means free-rider problems absent sustainable financing; universal access implies cross-subsidy from profitable to non-profitable users; the long-lived character requires an investor with a sufficiently low discount rate willing to fund infrastructure without immediate returns. **"No infrastructure is neutral and DPI is no exception."**

**Risks:** weak governance produces market concentration, opaque decision-making, and no public recourse when infrastructure fails or excludes.

**Policy responses:** mandatory interoperability frameworks; regulatory sandboxes; data fiduciary models; participatory governance via multi-stakeholder boards or public accountability mechanisms; long-term financial sustainability designed to prevent underfunding or capture; **adaptive governance structures** allowing iterative improvement, regulatory flexibility, transparency, and redress mechanisms for rapid error correction. The UNDP DPI Safeguards Framework (2023/2024) is the benchmark reference.

### 4.6 Crosswalk

[ECVD25, Annex] maps each of the eight infrastructural characteristics against the five design characteristics, marking cells as weak or absent. Notable "weak or no relationship" cells, useful for catching overclaiming:

- Standardisation ↔ non-rivalry
- Interoperability ↔ long-lived collective assets
- Data as high-value input ↔ essential inputs to a wide range of activities
- Public oversight ↔ generic/standardised capital services

---

## 5. Value assessment — the three-by-three matrix

**Purpose.** [ECVD25, §4] replaces cost-benefit analysis with a structured public value framework. Built on the RQIV model (reach, quality, impact, value for money; Coyle and Woolard 2010) crossed with the dynamic public value approach (Mazzucato et al. 2020).

### 5.1 Why CBA is rejected

CBA in principle applies **only to marginal changes**, whereas infrastructure investments change relative prices, reallocate factors of production, or change consumer preferences and business models. Standard econometric approaches omit spillovers. The derived nature of demand means returns often appear downstream — in sectors that *use* the infrastructure, not in it. Externalities and correlations drive a wedge between social and private market returns.

Documented shortcomings of CBA and value-for-money metrics: oversimplification of complex relationships (Ackerman and Heinzerling 2004); short-termism (Laverty 1996; MacKenzie 2016); a preference for **preventing government failure over proactive market-shaping** (Mazzucato et al. 2020); limited consideration of distributional effects (Adler 2011); and not having been updated for the digital economy (Coyle 2025).

**Analytical move.** Where a document justifies DPI investment on CBA or value-for-money grounds alone, treat this as a **methodological finding**, not merely a gap in ambition. The measure is structurally incapable of capturing what infrastructure does.

### 5.2 The three effect types

|  | **Direct** | **Dynamic** | **Market-shaping** |
|---|---|---|---|
| **Defining characteristic** | Operational and service efficiency gains within core DPI functions | Network effects, spillovers and cross-sector externalities expanding DPI impact | Structural transformation in industries, societies and market dynamics |
| **Core features** | Tied directly to functionality; efficiency and accessibility gains within primary users; emerges even without large-scale adoption; often measurable immediately | New use cases beyond original intent; interoperability and reusability expand effects across sectors; typically medium-term but can emerge quickly | Industry and state capacity shifts; alters power dynamics between governments, firms and individuals; durable and harder to reverse |
| **Why it matters** | Demonstrates short-term benefits; justifies early investment; informs risk mitigation in early rollout | Determines whether adoption scales; requires safeguards for fair access; spillover risks must be anticipated for regulation | Governments must proactively manage market dependencies; long-term policy must align with the economic shifts DPI creates |

**Two rules for using the matrix:**

1. **Categories are not rigid.** The same effect can occupy several categories depending on how it emerges and scales. Fraud and leakage reduction is *direct* when DPI immediately prevents unauthorised access to benefits; *dynamic* when scaled across sectors; *market-shaping* when lower-cost universal KYC expands credit access for underserved populations, drawing in new competitors. Assess not just where an effect starts but **how it evolves**.
2. **Time horizon correlates with the categories but does not define them.** Market-shaping effects can be rapid when a government mandates DPI use for payments; direct effects can take years as legacy systems phase out. Analyse the *conditions* that accelerate or delay effects — policy design, adoption speed, complementary infrastructure — rather than assuming a sequence.

Also distinguish **DPI-specific effects from amplified effects of ordinary digitalisation.** Simplifying paper processes is a generic digitalisation gain. Use three tests: does DPI provide shared, foundational services (infrastructure-level enablers); does it enable new interactions across sectors (cross-sector adoption); does it create dependencies that shape market structures (ecosystem dependencies)?

### 5.3 The three perspectives, with measures [ECVD25, Table 4]

**Direct effects**
- *Public sector/society:* uptake and use; operational cost-savings from reduced IT expense and procurement; programme leakages (fraud, duplication, inefficiencies); tax revenue; public servants' time saved
- *Individual:* coverage of enabled services (by gender, geography, income); administrative burden (time spent, procedural steps); satisfaction; user experience (error rates, downtime, ease of use); fraud or identity theft incidents; **reduction in frontline staff roles and in-person support** (risk for digitally excluded groups)
- *Industry:* cost-savings from integration; number of businesses using DPI; **human intermediaries removed**; revenue from DPI-based services (ID verification fees, KYC cost reduction); security vulnerabilities in private integrations; reduction in front-line service jobs

**Dynamic effects**
- *Public sector/society:* extent of interoperability across government systems; cost savings from digital interoperability; ability to detect and prevent corruption; improved policy targeting; time/cost savings launching new services on existing systems; net environmental impact (paper reduction vs. cloud energy)
- *Individual:* perception of government efficiency and transparency; trust in DPI security and privacy protections; citizen adoption (e-ID, digital payments)
- *Industry:* interoperability within government-facing business processes; cost/time reductions; net environmental impact; new businesses using DPI-enabled data and APIs; pricing shifts in DPI-enabled services; GDP impact

**Market-shaping effects**
- *Public sector/society:* government capacity to respond to crises; **shifts in reliance on private-sector DPI components** (vendor lock-in vs. digital sovereignty); role in economic formalisation (tax base via digital transactions); government leverage over digital markets; shifts in public-private governance models
- *Individual:* expansion of digital participation; **psychosocial impacts of reduced human interaction** in service delivery; longer-term public trust in government; shifts in citizen expectations of responsiveness
- *Industry:* new business models; economic formalisation effects on small businesses; **dual role in enabling competition vs. reinforcing market concentration**; international economic integration (cross-border payments); regulatory changes driven by adoption

**The framework does not assume the direction of economic change.** Costs, competition and other aspects may increase, decrease or stay the same depending on the starting point and design choices. Differentiated effects across the three perspectives have implications for overall economic value — an effect that is a saving for the public sector and a job loss for industry is not netted out silently.

### 5.4 RQIV within each effect type

Each cell can be interrogated on four dimensions:

- **Reach** — who is using it, how has adoption varied across groups, what is projected take-up? *Distributional* reach, not just aggregate. Examples: South Africa SmartID adoption 61% among over-60s vs. 38% among 46–60-year-olds, with cost cited as a barrier by 31% of rural vs. 18% of urban dwellers; Aadhaar penetration ~95% nationally (Jan 2025) but 62.9% in Nagaland, 78.8% in Arunachal Pradesh, 79.9% in Meghalaya. At the dynamic level, reach means **number of sectoral use cases enabled** — of 115 jurisdictions in IIPP's DPI Map, only 62 had digital identity enabling at least two sectoral use cases, meaning in almost half of implementations *the digital identity is not fulfilling any infrastructural role*.
- **Quality** — reliability, accessibility, user-friendliness, robustness. Beyond satisfaction (92% of 147,868 Indian respondents very or somewhat satisfied with Aadhaar; 81% would choose it given a choice), service quality metrics: authentication failure rates, downtime, accessibility for low-tech users. At the dynamic level, quality means the **quality and value of the data within the system** and who can access what, in what form.
- **Impact** — broader social and economic benefits. Direct: leakage reduction, fraud reduction, revenue collection (India's GST revenue grew by more than 50 basis points of GDP since 2018), time saved (Estonia X-Road: 15 min/transaction × 13m transactions in 2014 = 3,225 years saved; Niger cash transfers: ~1 hour travel and 3.5 hours waiting saved per transfer; Philippines: 80% reduction in time for new business permits). Dynamic: transaction cost reduction, GDP effects, efficacy of service provision.
- **Value for money** — cost to deliver (actual and contingent), savings generated, cost-effectiveness versus alternatives. Aadhaar rollout estimated at under $1.50 per enrolment ($1.5bn total, 2009–2013) — **but note this is a function of India's population size**; the calculus depends on population, existing infrastructure, state capacity for procurement and oversight. Dynamic VfM means **the change in cost of building services on top of the DPI** (India's Economic Survey: e-KYC reduced KYC cost from 12 to 6 US cents, though the methodology was not published; industry estimates of KYC cost range $13–$130 with no consistent measurement methodology).

**Evidence discipline.** [ECVD25] is candid that peer-reviewed studies are scarce, most focus on digital payments, and policy reports are "often methodologically limited". Quantified DPI impact claims should be attributed and their methodology interrogated — several widely cited figures have no published methodology.

---

## 6. Enablers and trade-offs

**Purpose.** [ECVD25, §5] — contextual conditions that determine how much of the theoretical value is actually captured. These are not caveats; they are variables.

### 6.1 Five enablers

1. **Trust in the data.** DPI is only as good as the data it runs on. Inconsistent records mean lost access to welfare, financial services or voting rights. Compounding: Nigeria's overlapping NIN, BVN and TIN systems created inefficiencies and made identity verification harder; risk rises when the DPI **does not fully replace previous systems**, allowing coexisting inconsistencies.
2. **Inclusive adoption and scale.** Without digital literacy, connectivity or prerequisite documents, DPI becomes a barrier rather than an enabler. **Digital divides don't just happen — they get reinforced.** Women in low-income countries are eight percentage points less likely to have an ID than men (World Bank 2021). Requires on-the-ground infrastructure, targeted literacy efforts, and feedback loops tracking usage across demographics.
3. **Complementary DPI.** Infrastructures have compounding effects. A country with digital ID *and* data exchange (Estonia) will show greater scaling and dynamic effects than one with only one. Evaluate from the outset whether other shared components already exist that can be leveraged — a systems-thinking approach.
4. **Country size.** Infrastructural characteristics imply decreasing marginal costs as more users and use cases leverage the infrastructure, so spillovers are likely more significant in larger populations. For smaller countries, capturing value requires strategic design choices — regional collaborations, open-source architectures, DPI as a packaged solution or DaaS — and assessment of partnership models, not just standalone feasibility.
5. **Local accountability.** DPI may over-centralise decision-making to the point where local officials lose the ability and accountability to address community-specific needs. Without accessible grievance redress, the system can *decrease* value at the individual level even where society-wide benefits prevail. In several countries it has fallen to civil society and the courts to raise issues on behalf of individuals locked out of digitised services.

### 6.2 Three trade-offs

**Sovereignty vs. strategic dependencies.** Sovereignty is usually understood as ownership, enabling resilience against external tampering, rent extraction and over-dependence. Two counterweights: (a) implications for **quality depend on local capacity** — lack of competition with international providers can produce poor service; (b) a country may fall under a **sovereignty illusion** if it is locked into service provision by international players or if there is market concentration at lower levels of the technology stack. DPI may deliver sovereignty at the software layer while cloud, security and hardware dependencies remain. Assess sovereignty as **long-term control over operations, standards and dependencies**, not ownership.

**Which competition effects to prioritise.** DPI can lower entry barriers for new firms in downstream markets, and government provision at low or no cost can level the playing field. But on the DPI layer itself, **natural monopoly characteristics are likely to exist**; whoever controls the infrastructure or its standards sets terms of access. Risk is pronounced where parts of the implementation are proprietary (biometric hardware) or switching costs are high (cloud). Competition must be considered in the layers **below** (enabling infrastructure) and **above** (applications and services with access to the DPI), not only at the DPI layer.

> *Calibration — both directions.* Brazil's PIX is associated with a significant and persistent decline in deposit market concentration, with small banks gaining deposit market power (Sarkisyan 2024). Conversely, India's Aadhaar/eKYC enabled Reliance Jio's disruptive entry into telecom, and UPI created a **duopoly** (PhonePe and Google Pay) on top of the infrastructure — while those same firms drove adoption. In African mobile money markets, large-scale interoperability policy lowered fees but also lowered private players' profitability, reducing investment in network coverage and towers in rural and poor districts, producing a **decline in several survey metrics of financial inclusion** (Brunnermeier et al. 2023). Interoperability is not monotonically pro-inclusion.

**Relational value vs. efficiencies.** DPI reduces transaction costs partly by reducing human intermediaries at scale, which may also lower corruption. But **in some societies and geographic/demographic contexts the relational aspect may be valued more than the efficiency gains**. Digital networks can enhance social connectedness but cannot fully replace physical interaction, particularly in community-oriented spaces. Governments must proactively provide alternative, easy-to-access in-person grievance redress, especially where internet penetration and digital literacy are low.

### 6.3 Distributional realism

The accurate picture of costs and benefits will be complex, and **the same intervention can produce opposite distributional outcomes in different jurisdictions**. A meta-study of biometric welfare authentication in India found that Andhra Pradesh and Jharkhand both reduced leakage — but in Andhra Pradesh benefits passed to beneficiaries as funds displaced from corrupt intermediaries translated into more money received, while in Jharkhand it produced "reduced disbursals from the government but did not improve the beneficiary experience in any way (and worsened it in some ways)" (Muralidharan et al. 2025). *Leakage reduction is not welfare improvement.*

A cross-country study of fast payment systems found adoption more widespread when the central bank owns the FPS, when non-banks participate, and when use cases and cross-border connections are greater: non-bank PSP participation associated with a 3.5% increase in FPS transactions per capita, each additional use case with 2%, each additional cross-border connection with 2%, and public ownership with 1.8% (Frost et al. 2024).

---

## 7. Synthesis and verdict

### 7.1 The output structure

An analysis using this framework should return, in order:

1. **Classification** — is the object infrastructure (Module 1), and at which stack layer? If not, say so and reframe the remaining analysis as service-level.
2. **Publicness diagnosis** — which rung of 'P'; which framing (attributes/functions/both); what the framing is silent on (Module 2).
3. **Directionality finding** — what direction is embedded, whether or not it is stated (Module 3, Pillar 1). *This is the single highest-value output of the framework.*
4. **Governance gap** — pillar-by-pillar, with the diagnostic questions answered or marked unanswerable from the document (Module 3).
5. **Mechanism trace** — for each design characteristic present, the economic mechanism claimed and the corresponding risk not addressed (Module 4).
6. **Value profile** — which cells of the 3×3 the document's evidence actually populates, and which it asserts without evidence (Module 5). Flag over-reliance on direct measures.
7. **Contextual conditions** — enablers absent, trade-offs unacknowledged (Module 6).
8. **Verdict** — against the closing test of [ECVD25]: *"the real test for DPI is not whether it is implemented, but whether it actively expands economic opportunity, enhances inclusion and delivers measurable public value."*

### 7.2 Failure archetypes

Named patterns to match against. Each has a distinct remedy, so classify rather than describing generically.

| Archetype | Signature | Source logic |
|---|---|---|
| **The neutral infrastructure** | Framed as a technical enabler; direction unstated and therefore unexamined; publicness rests on "public interest" without content | [MEV24] §4 — no infrastructure is neutral; unstated direction is still direction |
| **Attributes without direction** | Strong on open standards, reusability, open source; agnostic on outcomes; assumes spillovers will be positive | [MEV24] §4.2 — risks wasting investment in non-priority areas |
| **Function without attributes** | Clear social purpose; built as a closed, single-use, non-reusable system | [MEV24] §4.2 — wastes societal impact and is fragile to political shifts |
| **Values without governance** | Explicit and admirable public values; no process, no state role, no accountability mechanism | [MEV24] §4.2 — nothing intrinsic to attributes or functions creates inclusion, transparency or trust |
| **The CBA justification** | Investment case rests on cost-benefit or value-for-money analysis | [ECVD25] §2.1 — structurally cannot capture spillovers, non-marginal changes, or distribution |
| **Direct-measures-only** | Uptake, cost savings and satisfaction reported; no dynamic or market-shaping assessment | [ECVD25] §4 — measures short-term efficiency and calls it value |
| **Adoption as proof** | High adoption figures treated as evidence of value | Adoption is Reach, one of four RQIV dimensions, at one of three effect levels |
| **Sovereignty illusion** | Public ownership at the software layer; unexamined dependencies in cloud, security, hardware | [ECVD25] §5.2 |
| **The invisible population** | No distributional breakdown of reach; data quality treated as operational rather than policy | [ECVD25] §3.4, §5.1 — spectrum of visibility; high/low-resolution citizens |
| **Infrastructure in name only** | Digital ID or similar with no or one sectoral use case | [ECVD25] §4.3 — 53 of 115 jurisdictions on the DPI Map; fails Frischmann criterion 2 |
| **Efficiency over relation** | Human intermediaries removed as a headline benefit; no analogue or in-person fallback | [ECVD25] §5.2; [MEV24] §5.6 — universal access implies analogue access |

### 7.3 Prohibited inferences

Do not:

- Infer publicness from public ownership, regulation, or a stated public benefit.
- Treat "public interest" as if it had content.
- Accept a combined attributes+functions case as sufficient without governance.
- Net differentiated effects across public sector, individual and industry into a single figure without stating the distribution.
- Read leakage reduction as beneficiary benefit (see Jharkhand).
- Read interoperability as automatically pro-competition or pro-inclusion (see mobile money).
- Assume a direct → dynamic → market-shaping time sequence.
- Treat quantified impact claims as settled where the source is a policy report without published methodology.
- Conclude that value is absent because it is unmeasured — the frameworks exist because infrastructure value is systematically hard to measure, not absent.

---

## 8. Compressed reference

**The single sentence from [MEV24]:** if we want the 'P' to be public value maximisation, there is no DPI without explicit public values, governance following the five pillars of the common good, and a prominent, market-shaping role for the state.

**The single sentence from [ECVD25]:** DPI's value lies not in what it does but in what it enables, so its impact depends not just on what is built but on how it is governed and who benefits.

**The two-line bridge between them:** [MEV24] establishes *what makes DPI public* (normative, governance-first). [ECVD25] establishes *how to assess whether it delivers* (economic, measurement-first). Use [MEV24] for legitimacy, direction and governance questions; use [ECVD25] for design, mechanism and evidence questions. Where they overlap — non-neutrality, the insufficiency of technical attributes, the necessity of public governance — the claim is doubly supported and can be stated with confidence.

**Antecedents worth knowing.** Frischmann (2012) on infrastructure as shared means to many ends; Bozeman (2002, 2007) on public values vs. public interest; Moore (1995) on public value management; Sen (1985) on capabilities; Hess and Ostrom (2003) on the four types of economic good in the digital space (private / club / common-pool / public, on rivalry × excludability axes); Mazzucato (2013, 2016, 2023) on the entrepreneurial state, market-shaping and the common good; Coyle and Woolard (2010) on RQIV; Star and Ruhleder (1996) — *infrastructure is only such when or while it facilitates value.*

---

## Citation block for generated analyses

> Mazzucato, M., Eaves, D. and Vasconcellos, B. (2024). *Digital public infrastructure and public value: What is 'public' about DPI?* UCL Institute for Innovation and Public Purpose, Working Paper Series IIPP WP 2024-05. https://www.ucl.ac.uk/bartlett/public-purpose/wp2024-05
>
> Eaves, D., Coyle, D., Vasconcellos, B. and Deshmukh, S. (2025). *The Economics of Shared Digital Infrastructures: A framework for assessing societal value.* UCL Institute for Innovation and Public Purpose / Bennett Institute for Public Policy, IIPP Policy Report 2025/02. https://www.ucl.ac.uk/bartlett/publications/2025/mar/economics-shared-digital-infrastructures
