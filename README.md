<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero/system-map-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero/system-map-light.svg">
  <img src="./assets/hero/system-map-light.svg" width="100%" alt="Rakesh Singh — cloud and applied AI engineering for fintech and regulated products. 18+ years, up to 95% less deployment effort, $15M+ saved.">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/title-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/title-light.svg">
  <img src="./assets/headings/title-light.svg" width="100%" alt="Cloud and applied AI engineering for regulated products">
</picture>

I help fintech and enterprise teams design, migrate and ship production systems on GCP — combining platform engineering, data systems and applied AI.

[![Discuss an engagement](https://img.shields.io/badge/Discuss%20an%20engagement-C98A4B?style=flat-square)](mailto:ralphsin@gmail.com?subject=Engineering%20engagement) [![Selected systems](https://img.shields.io/badge/Selected%20systems-7FA3C9?style=flat-square)](#selected-systems) [![LinkedIn](https://img.shields.io/badge/LinkedIn-C98A4B?style=flat-square)](https://linkedin.com/in/rakesh-singh09)

> **18+ years** in production engineering · **Up to 95%** less deployment effort · **$15M+** cost savings delivered

<a name="start-where-you-are"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-01-start-where-you-are-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-01-start-where-you-are-light.svg">
  <img src="./assets/headings/head-01-start-where-you-are-light.svg" width="100%" alt="Section 01: Start where you are">
</picture>

<details>
<summary><b>You need a cloud architect</b></summary>

<br>

You have a migration, a landing zone or a platform that has outgrown its original shape, and you need someone who can hold the whole system in their head while still writing the Terraform.

**What that looks like:** current-state assessment → target architecture and control model → phased migration plan with explicit gates → reference implementation your team can extend.

**Relevant work:** [Gemini Enterprise platform enablement](#gemini-enterprise-platform-enablement--major-uk-telecommunications-enterprise) (GCP landing zone, identity federation, VPC-SC for an enterprise-wide AI rollout), [CloudMorph](#cloudmorph--migration-intelligence) (AWS to GCP migration architecture).

**Typical shape:** 6–12 weeks, architecture ownership plus hands-on delivery.

</details>

<details>
<summary><b>You are building an AI product</b></summary>

<br>

You have a promising demo and no path to production — the model is the easy part, and the evaluation, data controls, cost envelope and failure modes are the hard part.

**What that looks like:** structured LLM pipelines with deterministic boundaries → evaluation harness before feature work → schema-aware data access → cost and latency budgets treated as requirements.

**Relevant work:** [Transmute](#transmute--governed-conversational-sql) (text-to-SQL with a validation pipeline), [OpsMorph](#opsmorph--governed-incident-intelligence) (multi-agent incident investigation with a frozen, explainable confidence model), current fintech engagement (LLM-driven insights on GCP).

**Typical shape:** 8–16 weeks, from prototype to something you can put in front of a regulator.

</details>

<details>
<summary><b>You need someone to actually ship it</b></summary>

<br>

The design is agreed and the backlog is real. You need throughput from someone who does not need onboarding to be useful.

**What that looks like:** Python and FastAPI services, Terraform, CI/CD, test strategy, observability, and the unglamorous production readiness work that decides whether a launch holds.

**Relevant work:** [VerbaSync](#verbasync--multilingual-dubbing-pipeline) (event-driven pipeline shipped and tested solo), plus the delivery layer of everything above.

**Typical shape:** ongoing, part-time or full-time, remote.

</details>

<a name="how-the-pieces-fit"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-02-how-the-pieces-fit-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-02-how-the-pieces-fit-light.svg">
  <img src="./assets/headings/head-02-how-the-pieces-fit-light.svg" width="100%" alt="Section 02: How the pieces fit">
</picture>

```mermaid
flowchart LR
    A["Architecture<br/>constraints, controls, target state"] --> B["Platform<br/>landing zones, IaC, pipelines"]
    B --> C["Product<br/>services, data, applied AI"]
    C --> D["Operations<br/>observability, cost, readiness"]
    D -.->|"what production teaches"| A

    style A fill:#151B23,stroke:#C98A4B,stroke-width:2px,color:#E9EDF2
    style B fill:#151B23,stroke:#7FA3C9,stroke-width:2px,color:#E9EDF2
    style C fill:#151B23,stroke:#C98A4B,stroke-width:2px,color:#E9EDF2
    style D fill:#151B23,stroke:#7FA3C9,stroke-width:2px,color:#E9EDF2
```

Most engagements start at one of these four and pull in the neighbours. The loop back from operations to architecture is the part that usually gets skipped.

<a name="selected-systems"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-03-selected-systems-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-03-selected-systems-light.svg">
  <img src="./assets/headings/head-03-selected-systems-light.svg" width="100%" alt="Section 03: Selected systems">
</picture>

<table>
<tr>
<td width="50%" valign="top">
<a name="cloudmorph--migration-intelligence"></a>

**CloudMorph** — migration intelligence

Deterministic, phase-gated pipeline mapping AWS serverless to GCP-native services — three human approval gates, not one opaque translation step. **In production** at a global quick-service restaurant chain.

![Python 3.12](https://img.shields.io/badge/Python%203.12-C98A4B?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-7FA3C9?style=flat-square) ![Clean Architecture](https://img.shields.io/badge/Clean%20Architecture-C98A4B?style=flat-square)

[![View case study](https://img.shields.io/badge/View%20Case%20Study-C98A4B?style=for-the-badge)](https://github.com/ralphsin/cloudmorph-case-study)

</td>
<td width="50%" valign="top">
<a name="transmute--governed-conversational-sql"></a>

**Transmute** — governed conversational SQL

Schema-aware NL-to-SQL pipeline with a hard boundary between generation and execution — read-only by construction, PII-masked, cost-gated. **In production** at a global home-furnishings retailer: 30–40% better query accuracy, 40–60% lower LLM cost.

![Python](https://img.shields.io/badge/Python-C98A4B?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-7FA3C9?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-C98A4B?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-7FA3C9?style=flat-square) ![GCP](https://img.shields.io/badge/GCP-C98A4B?style=flat-square)

[![View case study](https://img.shields.io/badge/View%20Case%20Study-C98A4B?style=for-the-badge)](https://github.com/ralphsin/transmute-case-study)

</td>
</tr>
<tr>
<td width="50%" valign="top">
<a name="opsmorph--governed-incident-intelligence"></a>

**OpsMorph** — governed incident intelligence

Multi-agent investigation (Google ADK) with a frozen, explainable confidence model and deterministic evaluation — governed reasoning, not an open-ended agent loop. **Built for** a major US telecom operator.

![Python](https://img.shields.io/badge/Python-C98A4B?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-7FA3C9?style=flat-square) ![Google ADK](https://img.shields.io/badge/Google%20ADK-C98A4B?style=flat-square) ![Vertex AI (Gemini)](https://img.shields.io/badge/Vertex%20AI%20%28Gemini%29-7FA3C9?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-C98A4B?style=flat-square)

[![View case study](https://img.shields.io/badge/View%20Case%20Study-C98A4B?style=for-the-badge)](https://github.com/ralphsin/opsmorph-case-study)

</td>
<td width="50%" valign="top">
<a name="verbasync--multilingual-dubbing-pipeline"></a>

**VerbaSync** — multilingual dubbing pipeline

Event-driven serverless pipeline (Cloud Run + Cloud Tasks), planner → worker → stitcher per stage, two-phase bootstrap solving CI/CD's permission chicken-and-egg problem. **In production** for a global telecom operator: 95%+ test coverage.

![Python](https://img.shields.io/badge/Python-C98A4B?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-7FA3C9?style=flat-square) ![Cloud Run](https://img.shields.io/badge/Cloud%20Run-C98A4B?style=flat-square) ![Cloud Tasks](https://img.shields.io/badge/Cloud%20Tasks-7FA3C9?style=flat-square) ![Terraform](https://img.shields.io/badge/Terraform-C98A4B?style=flat-square)

[![View case study](https://img.shields.io/badge/View%20Case%20Study-C98A4B?style=for-the-badge)](https://github.com/ralphsin/verbasync-case-study)

</td>
</tr>
</table>

*Private source repos — `cloudmorph`, `transmute`, `opsmorph`, `verbasync` — sit behind each case study; access on request.*

<a name="current-engagements"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-04-current-engagements-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-04-current-engagements-light.svg">
  <img src="./assets/headings/head-04-current-engagements-light.svg" width="100%" alt="Section 04: Current engagements">
</picture>

### Gemini Enterprise platform enablement — major UK telecommunications enterprise

**Problem.** Rolling out an enterprise AI platform across a regulated telecom's GCP estate, spanning multiple business units, means clearing identity, security and data-residency gates before a single use case goes live, with legal, privacy and security stakeholders who need to see the reasoning, not just the diagram.

**Approach.** Principal Solution Architect role: GCP landing-zone integration for Gemini Enterprise (IAM, workforce identity federation, VPC Service Controls, Model Armor guardrails, CMEK, audit and observability posture), a governance layer (group-based licence allocation, connector governance, an Umbrella SIA/PIA framework), and adoption/FinOps visibility via Looker Studio — plus a working proof of concept wiring [Transmute](#transmute--governed-conversational-sql)'s existing governed pipeline into the platform as a registered agent, rather than rebuilding its governance from scratch.

**Status.** In delivery. Landing-zone and guardrail architecture cleared enterprise review; licences provisioned across business units; adoption dashboards and reusable architecture patterns in progress. No public repo yet — this is licensing and governance architecture, not a shippable codebase; a sanitised write-up is next once the design settles.

![Gemini Enterprise](https://img.shields.io/badge/Gemini%20Enterprise-C98A4B?style=flat-square) ![GCP landing zone](https://img.shields.io/badge/GCP%20landing%20zone-7FA3C9?style=flat-square) ![VPC Service Controls](https://img.shields.io/badge/VPC%20Service%20Controls-C98A4B?style=flat-square) ![Workforce Identity Federation](https://img.shields.io/badge/Workforce%20Identity%20Federation-7FA3C9?style=flat-square) ![Model Armor](https://img.shields.io/badge/Model%20Armor-C98A4B?style=flat-square) ![CMEK](https://img.shields.io/badge/CMEK-7FA3C9?style=flat-square) ![Looker Studio](https://img.shields.io/badge/Looker%20Studio-C98A4B?style=flat-square)

### Multi-tenant fintech platform — US fintech

**Problem/Approach.** Building a production-grade, multi-tenant financial application on GCP: LLM-driven insights, real-time pipelines, and infrastructure automation under regulated-data constraints.

![Python](https://img.shields.io/badge/Python-C98A4B?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-7FA3C9?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-C98A4B?style=flat-square) ![Cloud Run](https://img.shields.io/badge/Cloud%20Run-7FA3C9?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-C98A4B?style=flat-square) ![BigQuery](https://img.shields.io/badge/BigQuery-7FA3C9?style=flat-square) ![Terraform](https://img.shields.io/badge/Terraform-C98A4B?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-7FA3C9?style=flat-square)

<a name="telemetry"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-05-telemetry-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-05-telemetry-light.svg">
  <img src="./assets/headings/head-05-telemetry-light.svg" width="100%" alt="Section 05: Telemetry">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/generated/telemetry-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/generated/telemetry-light.svg">
  <img src="./assets/generated/telemetry-light.svg" width="100%" alt="Weekly-refreshed panel showing current focus, active stack and recent public activity.">
</picture>

<a name="how-i-engineer"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-06-how-i-engineer-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-06-how-i-engineer-light.svg">
  <img src="./assets/headings/head-06-how-i-engineer-light.svg" width="100%" alt="Section 06: How I engineer">
</picture>

![Deterministic where possible](https://img.shields.io/badge/Deterministic%20where%20possible-C98A4B?style=flat-square) ![Observable by design](https://img.shields.io/badge/Observable%20by%20design-7FA3C9?style=flat-square) ![Infrastructure as code](https://img.shields.io/badge/Infrastructure%20as%20code-C98A4B?style=flat-square) ![Secure defaults](https://img.shields.io/badge/Secure%20defaults-7FA3C9?style=flat-square) ![Explicit quality gates](https://img.shields.io/badge/Explicit%20quality%20gates-C98A4B?style=flat-square) ![Simple operational models](https://img.shields.io/badge/Simple%20operational%20models-7FA3C9?style=flat-square)

**Cloud and infrastructure** — GCP, Terraform, Docker, Cloud Build, Linux
**Backend and data** — Python, FastAPI, BigQuery, Firestore, SQLite
**Applied AI** — Gemini, Gemini Enterprise, structured LLM pipelines, text-to-SQL, evaluation
**Frontend** — TypeScript, Next.js, React, Tailwind
**Quality** — pytest, mypy (strict), Ruff, Playwright, Vitest

<a name="contact"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/headings/head-07-contact-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/headings/head-07-contact-light.svg">
  <img src="./assets/headings/head-07-contact-light.svg" width="100%" alt="Section 07: Contact">
</picture>

Open to selected remote engagements involving cloud platforms, data systems and applied AI.

[**Start a technical conversation →**](mailto:ralphsin@gmail.com?subject=Engineering%20engagement)
