# MASTER AUTONOMOUS AI-NATIVE DEVELOPMENT DIRECTIVE
# WPEssential Cart Rules Inspector for WooCommerce

**Specification ID:** WPCRI-MASTER-2026-11  
**Product name:** WPEssential Cart Rules Inspector for WooCommerce  
**Free slug:** `wpessential-cart-rules-inspector`  
**Pro slug:** `wpessential-cart-rules-inspector-pro`  
**Pro pricing hypothesis:** USD $89/year, one site (commercial configuration, not a verified market fact)  
**Status:** BUILD CONTRACT — NOT A CLAIM THAT A PLUGIN HAS BEEN IMPLEMENTED  
**Primary objective:** Deliver production-ready, separate Free and Pro WooCommerce plugins with reproducible diagnostic simulations, truthful evidence attribution, native WordPress UI, tested extension adapters, documentation, and marketplace submission evidence.  
**Language:** English for code, documentation, identifiers, UI defaults and developer communications. Internationalization required; no text hard-coded into rendering.

---

## 0. NONSTOP AUTONOMY CONTRACT — START ON READING, DO NOT WAIT FOR ROUTINE HUMAN CONFIRMATIONS

You are the Lead Autonomous AI Development Agent. This is an implementation assignment, not a request to propose a plan, mock up a few screens, or ask permission at every step. Upon reading this file:

1. Inspect the current repository, branches, code, commits, current working tree, manifests, tests, CI and any `.ai/` state. Do not overwrite real work or reset uncommitted changes.
2. Read this file completely; read `WPEssential_Cart_Rules_Inspector_START_AGENT.md`, `START_HERE.md` when present, and every companion contract under `docs/`.
3. Recover or initialize persistent memory, machine-readable tasks, dependencies, decisions, findings, blockers, evidence and current execution pointer.
4. Determine whether this is a new repository, partially completed product, or release candidate. Choose the lowest unfinished required dependency, not blindly Phase 0 if work exists.
5. Take the next executable task, change actual source files, run validation, fix failures, record evidence, update state and continue directly to the next unblocked task in the same active execution session.
6. Execute **only five consolidated phases P0–P4**, each with granular subtasks and strict exit gates. Do not eliminate required capabilities to reduce phase count.
7. Never stop simply because a task, subphase, planning document, screen, test or milestone is completed. Status reporting is not a stop command.
8. When a task cannot be finished due to a genuine external dependency, record a precise blocker, continue independent work, and distinguish implementation from release readiness.
9. Do not ask for design taste, naming variants, architecture preference, additional feature clarification or permission to proceed if this contract provides an answer. Resolve ambiguities through evidence, deterministic decisions and documented reasoning.
10. **Do not create a literal busy-wait loop.** “Nonstop” means continuous productive scheduling while the agent execution environment remains active. It cannot force a closed chat, expired tool session, revoked credentials or stopped runner to continue in the background. Persist a checkpoint enabling the next runner invocation to resume without re-planning or user repetition.

### 0.1 Non-negotiable limits

- Never execute real purchases, place paid orders, authorize refunds, modify live customer carts, activate/deactivate production third-party plugins, alter live prices, or perform external outbound billing actions for diagnostic purposes.
- Never claim the simulator is guaranteed side-effect free merely because it does not create an order. Third-party hooks can send mail, mutate stock/caches, call APIs or write database rows.
- Never claim a rule/source/plugin caused a price delta without the evidence specified in Section 5. Neither a callback's presence nor hook priority alone proves causation.
- Never claim universal third-party support. Claim support only with a versioned, tested adapter. Unsupported providers must be labeled clearly.
- Do not automatically submit, publish, pay for or sign marketplace/legal agreements; prepare complete ready-to-submit packages and indicate necessary authorized human actions.
- Never fabricate Composer, Playground, QIT, Plugin Check, E2E, security, benchmark or marketplace approval results.
- Do not store or export secrets, private customer details, payment instruments, tokens or live checkout session data. Default telemetry OFF.
- No human consultation for **routine AI engineering decisions**; genuine authorization, credentials, vendor accounts and high-risk production actions are separate permission boundaries.

### 0.2 Completion definition

The task ends only when all mandatory backlog tasks have accepted evidence; both plugin ZIPs are installable and tested, docs synchronized, vendor checklists prepared, and any unavoidable external blockers explicitly listed. If release gates are unmet, report incomplete honestly while working through remaining available tasks.

---

## 1. PRODUCT CONTRACT AND EXACT BOUNDARIES

### 1.1 User problem

WooCommerce stores may use multiple coupon, discount, conditional shipping, tax, currency, fees, role-pricing and gateway-dependent extensions. Merchants and developers cannot easily explain why a specific cart total resulted or which eligible/denied rule influenced it. Debugging often requires recreating checkout, toggling plugins, inspecting multiple settings pages, comparing logs and risking production side effects.

### 1.2 Product promise

“**Understand every total. Investigate every rule. Compare every change.**” A WooCommerce-native ADMIN/DEVELOPER cart calculation inspection workspace that executes supported test scenarios, displays exact observable totals, explains native coupon/shipping/tax eligibility, traces supported extension decisions, compares reproducible runs, and exports redacted evidence. No customer checkout surveillance.

### 1.3 Audience

Store administrators; WooCommerce support teams; agencies; extension developers; QA engineers; B2B wholesale pricing managers. Store managers need accessible explanations, developers need trace evidence and reproducible fixtures.

### 1.4 Explicit non-goals

Not a pricing rule creator, coupon generator, shipping plugin, tax advisory application, payment gateway, financial reporting system, A/B marketing service, checkout event recorder, general-purpose PHP profiler or production traffic analytics tool. Do not rewrite tax/discount/shipping calculations. Read WooCommerce's engine results as authoritative for the supported scenario context. Never silently modify storefront totals.

### 1.5 Delivery success metrics and truthfulness

Measure: scenario-to-repeatability ratio; reproduced coupon rejections; exact totals balance; adapter test coverage; UX task completion; overhead of diagnostic instrumentation when disabled; reproducible regressions; user-visible unknown attribution. Record actual results, never invent adoption, revenue or speed claims. Make features measurable, not marketing promises.

### 1.6 Functional scope matrix

**Free — fully functional independently:** isolated/test-only cart composer with product/variation/quantity selection; guest or permissible customer-context simulation; billing/shipping addresses; coupon validation and rejection reasons derived from WooCommerce core; standard line-item subtotal/discount/fee/shipping/tax/grand total breakdown; shipping zones/rates summary; tax rate/class summary; calculation status and unsupported-source warnings; one-off ephemeral runs; native admin dashboard, result details, basic diagnostics and privacy controls. It must be a useful plugin without Pro.

**Pro — separately installed addon requiring Free:** bounded, explainable calculation trace; provider-specific adapters and SDK; source attribution and evidence tiers; conflict hypotheses; saved versioned scenarios; baseline/current and A/B comparisons; batch scenario regression tests; advanced shipping/tax details; plugin compatibility matrix; redacted JSON/CSV/debug bundle exports; performance/timing; advanced diagnostics, filterable trace timeline, admin UX and retention. No fake premium features in Free, no bundled Free clone in Pro.

**Pricing:** One-site annual $89 is a proposal, not a feature gate, download payment integration or commitment to WooCommerce Marketplace commercial terms. Pricing config belongs in commercial metadata, not calculation code.

### 1.7 Source-of-truth decisions

- A WooCommerce engine-calculated amount may be labeled `observed`; exact source and rule identification requires vendor evidence.
- Preserved scenario inputs and captured outputs are separate immutable records; rerunning never overwrites an earlier run.
- A baseline is tied to product/variation IDs, price snapshots, WooCommerce/WP/PHP versions, settings fingerprints, adapter versions, currency, time context and other environment details.
- No false “100% trace” claim. Coverage and blind spots are user-visible.
- Production compatibility is evaluated and guarded; comprehensive third-party execution occurs in isolated staging.

---

## 2. PRE-DEVELOPMENT RESEARCH AND TECHNICAL VERIFICATION

Before source implementation, produce `docs/RESEARCH.md`, `docs/COMPATIBILITY_MATRIX.md`, `docs/RISK_REGISTER.md`, `docs/ARCHITECTURE_DECISIONS.md`, `docs/USER_JOURNEYS.md` and `docs/PRODUCT_REQUIREMENTS.md`. Research is a required task, not a reason to stop.

### 2.1 Competitive benchmarking targets

Investigate and document observed features, current status, product versions and verified links for: Checkout Simulator for WooCommerce; AlgolPlus Advanced Dynamic Pricing for WooCommerce and its debug panel; Tiered Pricing Table; DeftCoders Dynamic Pricing/Conditional Fees; Query Monitor; WooCommerce Conditional Shipping and Payments; WooCommerce core Shipping Debug Mode; Flycart Discount Rules; WooCommerce Dynamic Pricing; common cart/checkout fee and currency integrations. Distinguish public-documentation claims from installed, behavior-tested findings. Never assert undocumented absence.

### 2.2 Official standards to validate continuously

Confirm current official WooCommerce extension best practices, cart/checkout block server APIs, WC_Cart/coupon/tax/shipping APIs, hook lifecycles, HPOS compatibility, Plugin Check, WordPress.org plugin rules/readme format, Woo Marketplace requirements, QIT status, accessibility criteria, WordPress Playground Blueprint schema and Composer behavior at build time. Record date, source URL and tested versions. Do not trust stale memorized APIs. Avoid internal (`@internal`) WooCommerce classes.

### 2.3 Design and architectural spikes

Build minimal prototypes with tests before committing to the simulator strategy: safe execution environment boundaries; Cart/Checkout Blocks parity; coupon restrictions and exact rejection messages; tax-inclusive/exclusive rounding; multi-package shipping; hook stage snapshots; duplicate callbacks; active plugin introspection; failed third-party rule attribution; scenario serialization; enabled tracing latency. Retire failed spikes with evidence; preserve lessons in the decision log.

### 2.4 Compatibility tiers

- Tier CORE: official WooCommerce documented behavior with regression coverage.
- Tier VERIFIED_ADAPTER: specific plugin and version range tested with rule-level API/hook evidence.
- Tier OBSERVED_ONLY: totals, fees, discounts, rates and price changes but no dependable rule identity.
- Tier UNSUPPORTED: integration may affect totals but is not reliably observable; show warning and recommend staging-compatible test.

Every public compatibility claim must map to actual tests and a versioned evidence record. Do not impersonate an official vendor integration.

---

## 3. FREE / PRO SEPARATION AND DEPENDENCY LIFECYCLE

### 3.1 Two actual WordPress plugins

Create two installable packages: `wpessential-cart-rules-inspector.zip` containing `wpessential-cart-rules-inspector/`; `wpessential-cart-rules-inspector-pro.zip` containing `wpessential-cart-rules-inspector-pro/`. Each has its own main plugin header, namespace, Composer autoloader, build, translation domain, tests, README and lifecycle hooks. Pro declares a Free dependency/version contract and gracefully disables premium functionality if Free is missing or incompatible.

### 3.2 Ownership contract

Free owns: cart context builder, basic WooCommerce calculations, core coupon diagnosis, basic shipping/tax summaries, Free admin navigation, validated REST endpoint and permissions, transient run results and privacy-safe diagnostics, core architecture/contracts. Pro owns: trace persistency, adapters, plugin source fingerprints, conflict analysis, permanent scenario store and run history, comparisons, exports, regression runner, advanced logs, premium admin pages. Shared public interfaces are documented and stable; Pro registers extensions via public Free hooks/contracts rather than reaching into Free private internals. No hidden Pro source shipped in Free.

### 3.3 Installation matrix

1. Free only → fully functional Free, no fatal errors, no premium notices blocking work.
2. Free then Pro → capability negotiation and Pro navigation/routes become available.
3. Pro without Free → actionable admin dependency notice, no fatal, no activation crash.
4. Pro installed before Free → activate/resume when compatible Free appears.
5. Upgrade/downgrade, Pro deactivation, Free deactivation while Pro active, multisite, incompatible version → predictable, tested, read-only/protected state, no deleted user scenarios.
6. Two Composer vendors together → no global class, function or library collisions. Apply namespacing/prefixing strategies where necessary, especially shared vendor dependencies.

### 3.4 WordPress.org rules

Free must comply with WordPress.org requirements, be genuinely useful and not ship a disabled Pro codebase or misleading premium-only calls. License GPL compatible and document third-party assets/licenses. Pro licensing integration cannot block Free functions and must not send data without informed consent.

---

## 4. TECHNICAL REPOSITORY AND COMPOSER ARCHITECTURE

### 4.1 Suggested workspace

```text
repo-root/
├── WPEssential_Cart_Rules_Inspector_AI_Native_Master_Development_Prompt.md
├── WPEssential_Cart_Rules_Inspector_START_AGENT.md
├── START_HERE.md
├── .ai/{state.json,tasks.json,decisions.md,blockers.md,handoffs/,evidence-index.json}
├── plugins/
│   ├── wpessential-cart-rules-inspector/
│   │   ├── wpessential-cart-rules-inspector.php
│   │   ├── composer.json
│   │   ├── src/{Core,Domain,Cart,Coupons,Shipping,Taxes,Admin,REST,Infrastructure}/
│   │   ├── assets/, languages/, tests/, vendor/, readme.txt, README.md
│   └── wpessential-cart-rules-inspector-pro/
│       ├── wpessential-cart-rules-inspector-pro.php
│       ├── composer.json
│       ├── src/{Tracing,Adapters,Conflicts,Scenarios,Comparisons,Exports,Admin,Infrastructure}/
│       ├── assets/, languages/, tests/, vendor/, README.md
├── docs/{PRD,UI,ARCHITECTURE,API,COMPATIBILITY,TESTING,RELEASE}/
├── playground/blueprints/{base,free,pro,compatibility}/
├── scripts/{generate_readmes,build_playground_bundles,validate_blueprints,...}
├── tests/{unit,integration,e2e,fixtures,adapters,security,performance}/
├── .github/workflows/
└── dist/ [generated, not source]
```

### 4.2 Composer + PSR-4 — mandatory, both editions

Free `composer.json` maps `WPEssential\\CartRulesInspector\\` → `src/`. Pro maps `WPEssential\\CartRulesInspectorPro\\` → `src/`. Use real Composer with `composer.lock` pinned compatible packages. The main plugin bootstrap loads its own `vendor/autoload.php`; guard missing vendor with a safe admin error rather than fatal crash. PHPStan/PHP_CodeSniffer/PHPUnit as appropriate development dependencies. Production builds execute `composer install --no-dev --prefer-dist --optimize-autoloader` (or validated equivalent); exclude test/development packages, secrets and CI artifacts. Check GPL compatibility and vulnerability results for vendored libraries. Prefix conflicting third-party vendor symbols if needed; test Free/Pro together with other extensions.

### 4.3 PHP, WooCommerce and data layers

Use WordPress APIs, WooCommerce public APIs and stable extension points; PHP version floor must be justified against latest marketplace requirements and build CI. Do not pin fictional version support. Do not use raw SQL for customer/order manipulation, and never use `Automattic\\WooCommerce\\Internal` classes. HPOS compatible only once tested; this tool should not need to write orders. Test all supported product types and variations. Custom tables for scenario runs, events and comparisons may use `dbDelta` with migration/versioning and appropriate indexes; avoid autoloaded large WordPress option arrays. Use decimal-safe amounts/monetary representation, currency decimals and rounding explicit for comparisons. Avoid float equality for money.

### 4.4 Suggested bounded-storage model

- `wp_wpcri_scenarios`: scenario id, owner, visibility, name, input schema version, created/updated at, status.
- `wp_wpcri_runs`: immutable run id, scenario id nullable, snapshot version, environment fingerprint, status, finished at, retention expiry, error code.
- `wp_wpcri_events`: run id, sequence, stage, source, evidence level, relevant field paths, bounded JSON payload, duration, redaction status.
- `wp_wpcri_comparisons`: baseline/target IDs, canonical monetary delta JSON, changed context flags.
- `wp_wpcri_adapter_status`: adapter id, version, vendor version, verified range, last self-test outcome.
- `wp_wpcri_audit`: authorized create/delete/export/retention/settings actions, no secrets.

Use names that fit WordPress table prefix conventions and are vetted in implementation; above are logical entities, not permission to hard-code `wp_` in production. Free ephemeral data may be transient with bounded TTL rather than mandatory persistent records.

### 4.5 Backend contracts

Define versioned DTOs and public PHP interfaces: `ScenarioInput`, `CartContext`, `CartLine`, `RunRequest`, `RunResult`, `TotalBreakdown`, `CouponDecision`, `ShippingRateResult`, `TaxLineResult`, `TraceEvent`, `AttributionEvidence`, `AdapterCapability`, `ComparisonResult`, `DiagnosticExport`. Validate schema at REST boundaries. Every monetary event has currency and amount representation, stage, source evidence and provenance. No hidden direct UI-to-DB writes.

### 4.6 Permissions

`manage_woocommerce` for standard execution, stronger custom capability for diagnostic exports and advanced tracing where sensitive settings/plugins could be exposed. Separate `view`, `run`, `save_scenario`, `export`, `manage_adapters`, `manage_settings` granular capabilities. Current WordPress capability and nonce checks for admin actions; REST `permission_callback`; sanitize input/output; never assume nonce replaces authorization.

---

## 5. OBSERVABILITY CONTRACT — NO FABRICATED ATTRIBUTION

### 5.1 Event confidence taxonomy

`verified`: a tested adapter or WooCommerce authoritative native rule source gives the specific rule id, reason and contribution, corroborated with run evidence. `observed`: actual state/amount transition measured but individual source unknown. `inferred`: multiple observations suggest a cause; confidence limited, show alternative explanations. `unknown`: insufficient evidence, explicitly display unknown. `unsupported`: extension/context outside verified coverage. `error`: run failed; no derived success claim. UI, CSV and JSON all preserve same evidence level.

### 5.2 Stage evidence

Capture stable input and output data before/after permissible public WooCommerce hooks/stages; snapshots must be immutable, ordered and constrained by event count, memory and time budget. Examples: product/variation initial price; cart item effective price; coupon eligibility/result; coupon amount; fee records; shipping package/rate selection; tax base/rate/tax class; calculated total. Hook callback listing only provides candidate plugins; it cannot establish who changed the price. Never monkey-patch global hook dispatcher or reorder/remove arbitrary live callbacks to isolate providers on production.

### 5.3 Calculation parity and reconciliation

Produce canonical breakdown of item subtotals, item discounts, applicable taxes, fee amounts/taxes, shipping amount/taxes and final total. Different tax-inclusive/exclusive settings, line/item rounding, coupon allocation and currency precision require explicit handling. If balance does not reconcile, show `unexplained_delta` with original engine output and a warning; do not fabricate an accounting line to balance. Vendor-specific direct `calculated_total` overrides may create such a delta. Store raw evidence safely and use bounded canonical transformations for UI.

### 5.4 Side-effect and simulation isolation

There are two distinct claims: (A) a local engine recomputation reflects a given cart context; (B) it reproduces the exact live checkout flow with all extension behaviors. Do not conflate them. Document support tiers and limitations. Default run uses permissioned admin tool and dedicated ephemeral context; must preserve/restore current session state, globals, user context, locale and WooCommerce session if touched. Never interfere with actual customer sessions. External hooks may trigger side effects even in apparently isolated requests. For untrusted/unknown integrations or deep traces, require a disposable staging/Playground environment with outbound network/email controls, sanitized fixture data and test payment gateways; do not pretend an admin AJAX request makes execution isolated.

### 5.5 Repeatability and redaction

Capture product ids and selected variation, store currency, price snapshot, shipping zone, relevant settings fingerprints, customer-role context, tax exemption status, time assumptions, plugin version manifest (without private data), WooCommerce/PHP/WP versions, run mode and adapter capabilities. Saved baseline must state if reproducibility cannot be guaranteed. For deterministic fixture tests, freeze time only in isolated environment and only through explicitly tested adapter contracts; do not modify global production clock.

### 5.6 Failure behavior

Timeout, fatal third-party callback, thrown exception, invalid coupon, no shipping method, bad tax configuration, incomplete variation, version incompatibility and trace overflow produce **structured partial results with warnings** when possible. Never say `complete` if data is partial. Limit trace collection and truncate with explicit marker, not silent omission.

---

## 6. UI DESIGN CONTRACT — NO SCREEN MAY BE A PLACEHOLDER

### 6.1 Mandatory design system

Native WordPress/WooCommerce visual vocabulary: WooCommerce submenu (not unnecessary branded top-level menu), `@wordpress/components`, WordPress colors/typography/spacing, responsive admin layouts, accessible tables, WC notices and standard setting conventions. No decorative SaaS dashboard, pseudo-monitoring widgets, invented live-traffic metrics, excessive animations, neon charts or Photoshop-only UI deliverables. Implement actual usable PHP/React screens, not static HTML mockups. Interface must work with JavaScript disabled where essential server actions can reasonably fall back, and provide understandable disabled/error states.

### 6.2 Shared component requirements

Every screen: breadcrumb/title, role access rules, primary action, page description, context/help, real data, filter/search/sort where relevant, loading/empty/error/success/partial states, pagination for large collections, accessible focus order, keyboard interaction, readable contrast, translators' text domain, nonce and capability enforcement, responsive admin layout, dangerous-action confirmation, masked secrets and no false success messages. Explanations must distinguish core fact vs adapter evidence vs inference. No button may be inert. Every actionable control requires a real backend behavior, test and user documentation.

### 6.3 Precise screen inventory — implement every item

#### UI-001 — Dashboard / Overview [Free, enhanced by Pro]

**Location:** WooCommerce → Cart Rules Inspector → Overview. **Top action:** New Test Cart. **KPI cards:** recent runs (actual only), validation errors (only if available), last result status, installed adapter coverage (Pro), saved scenarios (Pro), unexplained deltas (Pro); no fictitious money volumes or shopper analytics. **Panels:** recent diagnostic runs (ID, scenario label, timestamp, total, currency, result/partial badge, action View); Getting Started (Create cart → Choose context → Run → Investigate); Environment notice (Woo active, checkout mode, feature support); Pro integration health when installed. **Filters:** date range, result type. **Empty:** first-test CTA. **Actions:** create new, re-open run if retained, duplicate context (Pro), purge own ephemeral results, open diagnostics. **Access:** `run` or `view` capability. **Test:** empty dashboard, real run refresh, Pro off, no WooCommerce active.

#### UI-002 — Test Cart Builder [Free]

**Layout:** main cart composer left 2/3, contextual settings/right recap 1/3; mobile narrow stacks. **Fields:** product search async by title/SKU/ID; selected variation dropdown/attributes; quantity integer >0; Add item, Remove item, Increment/Decrement, Clear cart; optionally custom item metadata if supported; customer context Guest / allowed existing test customer (never impersonate a real session); role where permitted; tax-exempt checkbox (only with capability); billing country/state/city/postcode; shipping country/state/city/postcode/address fields only where relevant; coupon input with Add/Remove; shipping rate package selector after rates loaded; payment method contextual selector if verified adapter; currency display, never unsupported arbitrary override; run mode Safe/Core or Isolated/Staging; advanced run timeout/capture budget. **Actions:** Validate Input, Run Test, Reset, Save Scenario (Pro), Copy Scenario JSON (Pro). **Validation:** missing product, invalid variation, quantity zero/negative, missing region, ineligible shipping address, unsupported currency, expired/unknown product. **Behavior:** changing input invalidates previous results; no actual order, checkout email or payment. Show privacy and side-effect risk message for plugins. **Empty:** add first product. **Results:** link to UI-003.

#### UI-003 — Calculation Results / Total Breakdown [Free]

**Header:** run ID, timestamp, scenario summary, PHP/WC/WP versions link, execution mode, coverage badge, rerun. **Summary:** currency, grand total, status, amount reconciliation, unexplained difference. **Breakdown table:** catalog subtotal, observed pre-discount price, line subtotals, item discounts, coupon discounts, fees, fee tax, shipping by package, shipping tax, item tax by class/rate, rounding and final amount. Distinguish discount value from base price change and avoid double-counting. **Item-level table:** product SKU/title, quantity, catalog unit price, calculation unit price, line subtotal, eligible coupon discount, tax class, line tax, row total. **Interactions:** expand row, view original vs effective price, source/evidence detail if Pro, copy summary, print-safe view, open coupon/shipping/tax inspector, rerun. **States:** full/partial/error/mismatched and supported vs unknown. **Tests:** tax-inclusive, mixed taxes, zero price, negative fees, multi-package, recalculation override.

#### UI-004 — Coupon Eligibility Inspector [Free]

**Search:** coupon code input, from-current-cart dropdown, Apply/Remove, Validate Eligibility, View Coupon Settings. **Checks grid:** existence, type/amount, usage limits, usage per user, expiration, allowed emails, min/max spend (show applicable base), product/variation exclusions, category exclusions, sale-item restrictions, individual use, free shipping eligibility, third-party restriction evidence. **Columns:** Check ID, actual, required, verdict, why, remediation. **Messages:** WooCommerce core errors use authoritative reason; third-party rejections not explained by core must be `unknown/plugin restriction` unless adapter evidence. **Actions:** test this coupon alone; compare before/after (Pro); reveal eligible products and discount allocations; open edit coupon if authorized. **Special cases:** product-specific coupons, multiple stacked coupons, repeated failed application, role restrictions, coupon code casing/encoding.

#### UI-005 — Shipping Inspector [Free basic; Pro deep trace]

**Sections:** shipping address with address completeness, shipping packages (each package and contents), matched core zone with id/name when supported, zone ordering context, available rates (method/instance/title/cost/tax), selected method, free shipping eligibility conditions, shipping class summary, pending/unavailable rates and provider timeouts. **Actions:** change shipping destination (returns to cart builder), rerun rate calculation, select available method, open zone settings with capability, expand package/rate. **Pro:** show adapter-provided exclusion/restriction explanation, differing rate stages, cache-context differences, possible conflicts. **Guard:** unavailable live carrier API may not be reproducible; label partial. **Tests:** no match, local pickup, free shipping min order with coupon, postcode constraint, multiple packages, per-class rates.

#### UI-006 — Tax Inspector [Free basic; Pro advanced]

**Header:** selected customer location and tax settings. **Tables:** product tax class, each tax rate label and percentage, tax base, item tax, fee tax, shipping tax, compound taxes and rounding mode. **Fields:** shipping/billing tax basis, exempt customer context, inclusive vs exclusive price settings, tax location, display currency/precision. **Actions:** change location in builder, rerun, open WooCommerce Tax settings (authorized only), inspect row/class, export calculations (Pro). **Caveat:** tax output is WooCommerce-computed evidence, not legal certification. **Tests:** mixed tax classes, tax-exempt, inclusive/exclusive, 0%/non-taxable rates, compound, multiple locations and rounding variation.

#### UI-007 — Execution Trace [Pro]

**Top controls:** run ID, start/end and duration, trace mode, capture coverage %, truncation badge, Search, Source Plugin, Stage, Evidence Level, Rule ID, Product/Line, Time Range, Show Unknown Only. **Timeline:** chronological event icon, observed stage, elapsed duration, before/after monetary snapshot, amount delta, Woo hook name, integration and version, rule ID/name only when verified, reason, evidence source, matched context and warnings. **Event drawer:** canonical JSON (redacted), cause/effect caveat, supporting rule events, callback list (if captured) explicitly marked non-causal. **Actions:** pin, copy reference, jump to relevant Woo settings, open trace limits, export redacted (capability), add to comparison. **States:** disabled, budget exceeded, partial trace, supported adapter vs unsupported. **Test:** no adapter, conflicting hook changes, callback no-op, trace overflow.

#### UI-008 — Conflict Center [Pro]

**Filters:** risk/severity, stage, source/unknown, run, status New/Investigating/Explained/Ignored, affected product/coupon. **List columns:** conflict ID, scenario, observed anomaly, evidence level, estimated financial delta (when reliable), possible providers, last detected, status. **Details:** symptom, precise evidence, at least two plausible explanations where inference is nonunique, reproduction steps, links to trace/scenario comparison, suggested safe troubleshooting steps, no automated plugin disable. **Actions:** mark investigated, add note, rerun in isolation, link compared baseline, dismiss with reason. **Special rules:** never falsely declare an extension buggy, never auto-fix prices/tax/shipping.

#### UI-009 — Saved Scenarios [Pro]

**List:** ID/name, tags, owner, created, last run, latest total/currency, environment stale marker, visibility, status Active/Archived. **Filters:** keyword, tags, owner, last status, product, date. **Actions:** New, Save, Duplicate, Rename, Run, Compare, Export, Archive, Delete (with impact summary and confirmation). **Scenario editor:** name, objective, cart lines, coupon codes, customer role context, addresses, preferred rate, tax context, time assumptions, tags, notes, expected total only if explicitly user-entered, version history and autosave. **Validation:** schema compatibility, missing removed product, private user contexts, stale plugin settings, nonreproducible time rules. **Permissions:** owner/team/admin visibility with capability.

#### UI-010 — Compare Runs [Pro]

**Selection:** Baseline A and Target B (saved scenario run or ad hoc), requirement same or explicit currency conversion policy, warnings if settings/plugins differ. **Side-by-side cards:** amount, timestamp, app versions, coupon, shipping, tax, evidence coverage. **Diff table:** line-by-line product prices, quantities, coupons, fees, tax, shipping packages, final total; absolute and percentage delta, stage changes, inferred vs verified source, environment changes. **Actions:** swap, choose baselines, pin findings, export report, retest A or B. **Special:** if inputs differ show `not an apples-to-apples comparison` and exact changed inputs; no silent currency conversion.

#### UI-011 — Batch Regression Runner [Pro]

**Fields:** select scenarios/tag groups, environment safe/staging, baseline selection previous verified run/latest pinned, tolerance according to currency smallest unit, max concurrency, time budget, stop-on-critical, adapter requirements, notification preference. **Job table:** queued/running/passed/failed/partial/cancelled with progress, retry, logs. **Actions:** Run Selected, Cancel, Resume with same idempotent job, compare failures, export summary. **Safety:** limited concurrency, no storefront impact, no forced live checkout execution; explicit staging-only for deep profiles. **Tests:** partial failure, interrupted worker, stale fixtures, duplicate start, idempotent retries.

#### UI-012 — Integration & Adapter Manager [Pro]

**Cards:** provider, installed version, adapter version, supported range, evidence coverage (rule IDs? eligibility? shipping? tax?), validated status, last test, limitations and link to integration guide. **Actions:** Run Self-Test (safe), Enable/Disable adapter (diagnostic only), View Configuration, Open Documentation, Report Unsupported Behavior. **Prohibited:** automatic third-party plugin activation/deactivation or outbound request without permission. **Compatibility levels:** tested/limited/observed-only/unsupported/broken. **Warning:** no 'supported' badge without version-specific tests.

#### UI-013 — Developer Exports [Pro]

**Fields:** select run(s)/comparison, export format JSON/CSV/Markdown diagnostic bundle, include trace yes/no, include version manifest yes/no, redact names/addresses/product names/IDs, trim stack traces, maximum export size, retention. **Preview:** sample redacted fields and warnings. **Actions:** Generate, Download, Copy Sanitized Summary, Delete Export. **Validation:** privilege and nonce, CSV injection mitigation, never export secrets/token values/raw customer personal data by default, only diagnostic information needed. **Export metadata:** schema version, checksum, timestamp, coverage and redaction markers. **Tests:** malicious coupon code, HTML/XSS strings, private product titles, no permission, very large event store.

#### UI-014 — Settings [Free + Pro]

**Free tabs:** General (feature toggle, notice level, default execution safe mode), Privacy (TTL, data retention, telemetry disabled by default, personal data redaction), Calculator (supported currency behavior, failed run timeout), Permissions (who can run/view), Troubleshooting (Woo logs link), Appearance (WordPress native only; no unnecessary theme engine). **Pro tabs:** Trace (enabled only on manual admin tests, max events/time/memory), Scenario retention, Adapter capabilities, Comparison thresholds, Export redaction, Batch test caps and notification rules. **Actions:** Save, Restore Defaults (with confirm), Validate Configuration, Export non-sensitive settings, Clear expired data. **Tests:** capability enforcement, invalid settings, Pro off, migration and uninstall.

#### UI-015 — Tools & Diagnostics [Free + Pro]

**Sections:** active WooCommerce status, PHP/WP/WC versions, WC cart/checkout mode, HPOS declaration/test notes, session isolation warnings, installed relevant plugins, PHP extensions, schema versions, last errors without secrets, memory/task limits, Playground/isolation recommendations, self-test fixtures. **Actions:** Run Safe Self-Test, Download Sanitized Environment Summary (Pro), Inspect Logs, Clear Expired Runs, Repair Schema (guarded), Verify Hooks/Adapters. **Output:** pass/warn/fail with evidence link and version, not false generic green checks.

#### UI-016 — Result Side Panel / Explanation Drawer [Free + Pro]

Every numeric total/fee/coupon/shipping/tax row opens a consistent explainability drawer: title, amount+currency, source/evidence level, applicable rules, data path, authoritative settings when known, timeline evidence (Pro), `why this amount` text, uncertainty and limitations, 'open setting' (authorized only), 'compare' (Pro), copy explanation, accessible Close. Do not default attribution to the first callback.

#### UI-017 — Setup / First Run Wizard [Free]

**Steps:** Environment check, Privacy+Safety acknowledgment, Optional demonstration test fixture (dummy products only; no automatic creation on production), Guide to selecting product/address/coupon, Run test, Open result, Finish. **Actions:** Next, Back, Skip, Recheck, Open Help. No forced account signup or SaaS integration. Display staging recommendation before enabling deep third-party tracing.

#### UI-018 — Supported Adapter Detail / SDK Diagnostics [Pro]

**Fields:** provider and plugin version, version constraints, supported stages, known limitation list, self-test fixtures, event schema, evidence provenance mapping, coverage matrix, installed hook/API identifiers and test evidence. **Actions:** validate adapter contract, run sandbox adapter test (only permitted safe environment), export adapter validation report, show developer integration documentation. Render missing vendor APIs as unsupported rather than passing.

### 6.4 UI design QA gate

For **each** UI ID above, create `docs/UI/UI-xxx.md`: navigation, persona, goal, exact fields with type/default/min/max/format/help/validation, search/filter/sort/table columns, primary/secondary/danger actions, popup/drawer behavior, loading/empty/partial/error/permission/Pro-off states, server contract and capabilities, mobile stacking, keyboard behavior, screenshot(s), accessibility test and E2E test ID. Build wireframe in code before applying polish; use real fixtures; verify with browser screenshots at normal desktop and narrow width; inspect for cut-off, overlapping text, incorrect labels, fake buttons. Never submit screenshots of unimplemented UI as proof.

---

## 7. COMPLETE FREE WORKFLOWS — EXACT ACCEPTANCE BEHAVIOR

### W-F01 — First install and safe onboarding

Free activates only with WooCommerce, explains requirement when missing and never hard-crashes. First-run wizard confirms capabilities, minimum versions, privacy, isolation limitations, and suggests a dummy cart fixture. User may skip onboarding and access tool. Storefront must remain unaffected.

### W-F02 — Build and execute single test cart

Search active/catalog-accessible product, choose variation, set qty; validate product and current price; choose customer role context without hijacking a user session; enter address and coupons; collect server-side WooCommerce calculation; report exact totals and evidence coverage; preserve current admin context and restore temporary state. No actual purchase or order. Re-run after input change; ensure stale indication; fail gracefully on unavailable service.

### W-F03 — Coupon accepted or rejected

Core coupon reasoning uses WooCommerce's current official eligibility/validation behavior. Present explicit actual-vs-required input for minimum/maximum spend, usage, sale item, product/category and email restriction where safe. Supported coupon may be applied in test context without changing usage count; verify this invariant with a real integration test. If plugin-specific hook rejects coupon with no exposed reason, label source unknown.

### W-F04 — Shipping and tax calculation

Set address, calculate all packages and rates through supported WC APIs, select a real offered rate, show zone/option source when public API reveals it, then tax class/rates/base/rounding. Omit cart-level shipping if no shipping is needed (all virtual). Multi-package carts must aggregate without losing per-package explanation. If plugin contacts real carrier API, recommend isolated staging or clearly show unverified external effects.

### W-F05 — Results and warnings

Display totals and exact core calculations, no unsupported invented causes. Show inaccessible shipping/invalid customer address/currency/third-party limitations as partial. Provide accessible explanation drawer and self-test. Results not stored long-term in Free unless explicitly chosen retention permits ephemeral cache.

### W-F06 — Free activation, uninstall and privacy

Deactivate without storefront impact; don't wipe saved Pro scenarios when Free is removed; avoid autoloading large diagnostic results; support WordPress privacy workflows and explicit removal preferences; never send telemetry by default.

---

## 8. PRO END-TO-END WORKFLOWS

### W-P01 — Bounded execution trace

Enable in an explicit diagnostic run; record stage snapshots, hook and adapter events ordered with time budget. Capture unsupported callback list as diagnostic **not proof**. Display observed deltas, verified rule IDs, omitted data warning, source confidence, truncated events and partial results. Never hook into all shopper checkouts persistently.

### W-P02 — Third-party rule adapter execution

Adapter detects provider/version/feature capabilities, registers to *documented public* extension points, converts provider events into versioned trace DTOs, labels proof, and self-tests against fixtures. If expected event never fires, do not invent one; return limited mode. Expose `adapter_health` result.

### W-P03 — Conflict hypotheses

Run mismatch-detection strategies: duplicate-looking fees, adjusted item prices without verified source, discount stacking anomalies, shipping threshold transitions, tax base changes, same-input nondeterminism, checkout-versus-admin discrepancies. Correlate evidence into hypothesis, assign `verified` only to directly attested details; otherwise inferred and show alternatives. Never disable other plugins or rewrite financial settings automatically.

### W-P04 — Saved scenario and snapshots

Create one scenario with labeled cart/context; save version; immutable run with environment fingerprint; rerun with identical or changed context; surface changed product prices, plugin versions, tax/shipping policies and time dependence; define owner/visibility, permissions, retention and delete. No raw personally identifiable customer data in exports.

### W-P05 — Compare A/B

Select two run IDs; normalize to canonical currency decimal rules (never convert silently), calculate exact differences by item/fee/coupon/tax/shipping and full total, show changed inputs and environment. If unlike-for-like, prominent warning. Provide timeline/adapter attribution where verified and export redacted report.

### W-P06 — Batch regression

Select scenario group, choose pinned baselines, queue bounded jobs in Action Scheduler or validated equivalent, execute safely in approved environment, mark PASS/DIFFERENT/PARTIAL/ERROR, recover retries idempotently, report output and budget/timeouts; no unbounded high-traffic runs.

### W-P07 — Developer support report

Choose run/comparison, preview redaction, export JSON/CSV/Markdown with schema/version/evidence coverage, hook/adapter names where appropriate, checksum, repro input and expected vs actual. Prevent spreadsheet formula injection and customer data exposure.

### W-P08 — Pro downgrade, upgrade and retention

Premium UI disappears safely when Pro deactivated; Free remains usable; scenario data may remain dormant until approved retention cleanup; reactivation migrates versioned schema; no paid key leaks; audit sensitive config/exports; account for WordPress multisite and HPOS compatibility.

---

## 9. THIRD-PARTY ADAPTER AND COMPATIBILITY PROGRAM

### 9.1 Required interface (conceptual contract)

Every adapter must expose stable identifier, display name, provider plugin identifier, supported version range, capability set (`rule_id`, `eligibility_reason`, `discount_amount`, `shipping_restriction`, `tax_adjustment`, `fee_reason`), availability check, registration/disposal, sanitized event normalizer, safe/isolated-mode requirement, own fixtures and self-test result. Use core extension interfaces, version negotiation and predictable error DTOs. Do not rely on private source-code monkey patches or unlicensed vendor API scraping.

### 9.2 Initial priority list and honest scope

1. WooCommerce core coupons, cart totals, shipping, fees, tax — default Free coverage, exhaustive engine behavior tests.
2. AlgolPlus Advanced Dynamic Pricing — investigate documented debug/public extension APIs and obtain precise attribution only when reliable.
3. Flycart Discount Rules — evaluate public hooks and rule metadata; use observed-only when no stable contract.
4. WooCommerce Dynamic Pricing — same versioned procedure.
5. Tiered Pricing Table — investigate pricing decision and tier conditions.
6. Conditional Shipping and Payments — investigate native extension debug data and restrictions.
7. Advanced Coupons/Smart Coupons — validate stacking, extended conditions and core-plus-vendor reasoning.
8. Common currency-switching, WooCommerce Tax, shipping carrier rates, bundles/subscriptions — separate compatibility specs and regressions; do not assert broad support prior to testing.

Priorities are targets, not false compatibility promises. If a paid plugin license/test installer unavailable, record `external_fixture_unavailable`, implement and test public adapter contract using safe fixtures without claiming verified vendor behavior, and progress other tasks.

### 9.3 Adapter acceptance tests

Plugin absent, wrong version, plugin installed but inactive, version within range, rule applies, rule fails, plugin changes price with no event, repeated run, duplicate hook, manual code exception, timeouts, cross-plugin interference, privacy redaction, disabled adapter, unsupported vendor. Each claimed version range requires actual tested fixtures and documented evidence. Adapter never changes rule priority or interferes with production checkout.

### 9.4 Developer adapter SDK

Ship reference API docs, minimal complete example adapter, schema validation, unit fixtures, integration harness, capability registration lifecycle, error codes, test invocation instructions, semantic version policy and coverage table. Mark any sample data as demo; never advertise the demo adapter as verified commercial integration.


---

## 10. REQUIRED SECURITY, PRIVACY AND PERFORMANCE

### 10.1 Authorization and data boundaries

Only authorized administrators/developers can run sensitive diagnostics. Guest/public REST endpoints must never expose plugin lists, pricing rule configuration, customer data, coupon restrictions or private product details. Avoid production customer impersonation; role testing must use a safe reproducible context and refuse elevated privileges. Use server-side capabilities and nonces; escape HTML and attributes; parameterize SQL; secure file exports via authorized expiring download routes. User data removal/retention must be documented and testable.

### 10.2 Scenario side effects

Define a `RunSafetyPolicy` with `mode`, `execution_environment`, `third_party_capabilities`, `network_request_policy`, `max_duration`, `max_events`, `max_memory`, `max_line_items`, `max_batch`, `mail_policy`, `payment_policy`, `customer_session_policy` and `reversibility`. A test on live admin cannot guarantee all arbitrary plugin effects; screen should show explicit warning when deep runs are restricted to staging. Never implement broad hook suppression that changes the pricing result. Test accidental order writes, coupon usage mutation, stock decrements, email triggers and PHP session leakage. Failing any such safety test is a release blocker.

### 10.3 Time and scalability

Every diagnostic request bounded with timeout, event size and memory budget; nested cart calculations avoid uncontrolled reentrancy; no global indefinite traces. Scenario lists paginated; events stored with indexed run ID and sequence; batch scheduler has quotas, cancel/resume and backpressure; unused runs purged by retention policy; high-volume UI tables avoid N+1 queries. Capture execution timing without pretending exact profiling of arbitrary third-party internals. Pro disabled = negligible storefront overhead; measure with automated fixtures.

### 10.4 Compatibility

Test active-store plugin sets, multisite (if declared), supported PHP versions, WP/WC latest and previous major versions, Classic Cart/Checkout vs Cart/Checkout Blocks, HPOS on/off if order APIs touched, tax automation providers, multiple currencies, RTL/i18n and standard admin accessibility. Do not declare HPOS/Blocks support until tested. Preserve storefront behavior with plugin disabled/enabled.

### 10.5 Logging and audit

Diagnostics logging opt-in, use WC_Logger or documented Woo logging conventions when appropriate. Redact secrets, customer PII, gateway credentials and unexpected sensitive HTTP responses. Admin action audit contains user ID where allowed, timestamp, capability-checked action, object ID, summary and completion status. Support cleanup and site privacy policy documentation. Support debugging without collecting shopper traffic.

---

## 11. AI-NATIVE TEAM: SPECIALIZED AGENTS AND HARD RULES

Maintain role descriptions under `docs/AI_AGENTS.md`. Even if only one coding model is available, it must execute these roles sequentially, maintain review separation and not claim independent-agent approval if none occurred.

**A01 Lead Orchestrator / Product Owner:** owns master contract, task dependency graph, status, architecture decisions, conflict resolution, next task selection, release completeness. Never leave the next-task pointer stale.

**A02 Technical Researcher:** verifies latest Woo/WP official APIs, competitor facts and extension version contracts; cites primary sources in research docs. Never assume internal API stability.

**A03 Systems Architect:** owns Free public contracts, Pro dependency edges, schema, namespaces, simulation isolation, trace model, module boundaries and compatibility spikes. Never compromise evidence taxonomy.

**A04 Free Backend Engineer:** WooCommerce cart builder, core calculations, coupon/shipping/tax diagnoses, Free REST and backend validation. No premium logic in Free release.

**A05 Pro Backend Engineer:** event trace, scenarios, comparisons, regression scheduler, exports, Pro lifecycle. No direct Free internals coupling.

**A06 Integration/Adapter Engineer:** vendor-specific adapter verification, version matrix, fixture harness, SDK and failure modes. No untested support claims.

**A07 UI/UX Product Designer:** produces each screen's complete field/action/state spec and WordPress-native design language; reviews UX task flows and accessibility. Never give a screenshot with missing functional controls as a finished screen.

**A08 Frontend Implementer:** WordPress components, React/TypeScript where needed, tables/forms/drawers, translation, keyboard behavior, async states, backend integration. No inert controls or fake data after production wiring.

**A09 QA/E2E Engineer:** unit/integration/browser tests, fixture data, plugin conflict scenarios, Classic/Blocks parity, Playground and real DB tests; logs all failures with reproduction steps.

**A10 Security/Privacy Reviewer:** auth, nonce, XSS, SQL injection, export redaction, PHP side effects, PII, DOS and retention tests; release STOP if critical.

**A11 Documentation/Marketplace Engineer:** verified manifest, readme.txt/README.md generation, end-user and developer docs, WP.org and Woo Marketplace checklists, screenshots and distributable ZIPs.

**A12 Release/CI and Independent Reviewer:** reproducible Composer builds, Plugin Check/QIT when available, cross-tier installation, artifact checksums, provenance, final acceptance matrix; verify that implemented code actually matches spec and screenshots.

### 11.1 Rules binding ALL agents

- Source-of-truth order: security/safety boundaries > verified current official platform requirements > this Master contract > decisions logged with evidence > backlog task spec > local implementation convention.
- Never change Free/Pro boundaries without written decision and regression evidence.
- Every requirement maps to at least one task, test and owner; no orphan feature; no duplicate implementations.
- An agent may review a different agent's work; self-review must be identified honestly.
- Never mark `done` based on TODO comments, generated placeholders, screenshots, stubs, passes without assertions, or unavailable tooling.
- If blocked by unavailable external dependencies, document exactly what cannot be verified and finish everything else.
- No user consultation for routine technical choices; human approval only when necessary for irreversible external actions/permissions.
- When design feedback suggests changes, log rationale, update screenshots/acceptance tests; continue implementation automatically.

### 11.2 Universal task record

Task ID, phase, module, tier, exact requirement, primary agent, dependencies, acceptance criteria, test IDs, file paths, status (`pending|in_progress|blocked|failed|done`), attempts, last error, completed_at, commit, evidence links, decision references, next retry conditions. Every task is atomic enough to be completed with useful evidence in an agent session; break overlarge tasks into tracked children while preserving requirement IDs.

---

## 12. AUTONOMOUS NONSTOP TASK LOOP AND RECOVERY

### 12.1 Required loop algorithm

```text
BOOT:
  inspect repository + git status + current files
  read MASTER and START_AGENT, source registry, .ai state
  if absent: initialize state and task graph from committed templates
  validate state consistency against real files and git history

WHILE execution runtime is available:
  choose highest-priority unblocked task whose dependencies are done
  if none:
     reconcile task graph, investigate blockers, validate current phase gates
     if all release gates passed: create final evidence report, finish
     if real external blockers: record them; continue unblocked documentation/tests
     do not spin uselessly; checkpoint and stop with honest blocker if no work possible
  record task in_progress and checkpoint
  research required API (if needed), implement actual working changes
  run its tests + static checks + relevant integration/E2E checks
  on failure: diagnose, patch, re-run, record exact evidence
  on success: update task status, decisions, artifacts, state, next_task
  commit verified milestone if permissions available; do not rewrite unrelated changes
  immediately select NEXT task without requesting "continue"
  report succinct milestones without treating report as an interruption
ON expiration/interrupt:
  write durable handoff, exact next command/task pointer and evidence paths
```

**Never run `while true` without bounded productive work.** Host may limit runtime and tool calls. A prompt cannot promise physical background execution without a persistent runner. The state/recovery system is how the next session proceeds without repeated human planning.

### 12.2 If blocked or ambiguous

1. Check Master/official docs/tests; choose conservative supported behavior.
2. Document decision in `.ai/decisions.md` with competing options, evidence, tradeoffs, rollback and tests.
3. If dependent on missing vendor plugin credentials, keep that adapter unverified, build mock contract tests, and continue unrelated work. Do not mark vendor compatibility as verified.
4. If repository read-only or no push access, make local commits/patches if possible, generate output package, and record inability to push.
5. If production/live action requires authorization, never execute it; complete staging/local tests and report actionable manual gate.
6. If retry repeated failure crosses configured limits, mark task `blocked`, capture root cause and next trigger, and continue independent tasks. No silent abandonment.

### 12.3 Exact persistent files

- `START_HERE.md` — human-readable current phase, verified progress, exact next task, necessary command(s), blockers, latest evidence and release gates.
- `.ai/state.json` — versioned machine state with current_phase, active_task, next_task, last_verified_commit, last_test_run, completed/blocked counts, worktree hash, last_updated_utc, release_gate_status.
- `.ai/tasks.json` — canonical machine-readable granular backlog and dependency graph.
- `.ai/decisions.md` — durable architectural and design decisions.
- `.ai/blockers.md` — blockers, owner, attempts, prerequisites and parallel work.
- `.ai/handoffs/YYYYMMDD-HHMMSS.md` — environment-specific last actions, commands, branch, files, tests, risk, exact next call.
- `.ai/evidence-index.json` — task/test ID → execution artifact/checksum/timestamp and real pass/fail/skip.
- `docs/STATUS.md` — concise release dashboard; regenerate from canonical task state rather than manual contradictory edits.

No secrets/API keys in any repo file. Never overwrite existing actual memory from templates. If state contradicts source/tests, repair via source evidence first. After git pulls or branch changes, recompute next_task by comparing commits/task acceptance, not from untrusted stale memory.

### 12.4 No repeated start prompts

First invocation reads both instruction files and executes. Every follow-up invocation reads `START_HERE.md` and resumes. Agents must not end every response with “Shall I continue?”; they continue when their runtime supports it. If a chat terminates, they cannot run asynchronously by force: persistent state enables one clean resume request in a subsequent active runner session. Never promise guaranteed background completion.

---

## 13. ONLY FIVE CONSOLIDATED DEVELOPMENT PHASES — ALL REQUIREMENTS STILL MANDATORY

### PHASE P0 — DISCOVER, VERIFY, DESIGN AND BOOTSTRAP

Inspect repo; read instruction files; recover state/backlog; competitor benchmark; official platform docs; security and compatibility constraints; architecture decision records; safety runner proof-of-concept; adapter contracts; canonical monetary/event schemas; Free and Pro composer scaffolds; minimum migration mechanism; Playwright/WordPress Playground/DB infrastructure; CI skeleton; UI navigation, component system and exact screen specifications; dependency graph. **Exit gate:** clear architecture, source tree, spike evidence, all screens specified, first executable Free task, persistent state and build/test CI commands—not just a PowerPoint mockup.

### PHASE P1 — COMPLETE INDEPENDENT FREE PLUGIN

Implement plugin lifecycle, Composer PSR-4 autoloading, WooCommerce dependencies, Free dashboard, onboarding, test-cart builder and context validation, real WC cart/coupon/shipping/tax calculations, detailed result and explanation drawer, core eligibility and rejection reasons, basic diagnostics, REST auth, retention, native accessibility, translations, tests and documentation. Free must work without Pro; no fake Pro stubs in Free. **Exit gate:** installable Free ZIP on Playground and supported MySQL WordPress, no storefront changes, all Free UI and test scenarios verified. No proceeding with unsupported Free architecture to mask failures.

### PHASE P2 — COMPLETE DISTINCT PRO PLUGIN AND ADAPTER PROGRAM

Implement Pro dependency/version negotiation, trace events, attribution evidence, event budget, adapter SDK, verified vendor-specific adapters when fixtures available, observed-only fallback, conflict center, saved scenarios/versioned runs, A/B comparison, batch regression runner, diagnostics/export/redaction, privacy/retention, UI Pro surfaces, upgraded settings, extended docs and E2E. **Exit gate:** real Free+Pro ZIP installations; Pro functionality tested end-to-end; all unavailable vendor claims marked unverified, with required contracts complete. Commercial Pro value must go beyond simple hook listing.

### PHASE P3 — CROSS-ENVIRONMENT TESTING, SECURITY, PERFORMANCE AND REPAIR

WordPress Playground Blueprint profiles; actual PHP/WP/WC version matrix; WooCommerce Blocks and Classic tests; real MySQL/MariaDB transactional/context tests; both plugins together and separately; vendor adapter fixture verification; collision and user isolation; privacy/security static checks; UI screenshots and keyboard accessibility; profile trace disabled overhead; scenario runner side effects; 50+ critical negative cases; fix/retest loop; threat modeling; release risk assessment. **Exit gate:** critical severity 0 unresolved, no unsubstantiated compatibility, all must-pass test evidence, documented skipped vendor tests where external prerequisites absent.

### PHASE P4 — VERIFIED DOCS, PRODUCTION PACKAGING, MARKETPLACE EVIDENCE

Generate Free `readme.txt` and both `README.md` from tested feature manifest; changelog, FAQ, requirements, installation, uninstall, privacy, API/adapter docs, translations, screenshots (from actual working UI); installable separate Composer-optimized ZIPs; WordPress.org Plugin Check/readme validation, plugin directory metadata, GPL notices, no unsupported ads; Woo Marketplace Pro QIT/local equivalents, HPOS/Blocks declarations only if tested, onboarding/reviewer instructions, downloadable demo fixtures, vulnerability checks, licenses and checksums. Prepare submissions, but do **not** submit or pay without authorization. **Exit gate:** all release evidence recorded and verified with reproducible commands, external marketplace/vendor account gates clearly identified, clean source and output artifacts.

**Important:** 5 phases are consolidated only for management; all granular tasks from registry remain compulsory. Do not mark a phase complete while its critical task has only a plan or screenshot.

---

## 14. TESTING CONTRACT AND MUST-PASS SCENARIOS

### 14.1 Test layers

PHP unit/domain tests; WooCommerce/WP integration using real public APIs; multi-PHP/version matrix; REST permission and input validation; composer namespace collision; WordPress Playground smoke and interactive browser E2E; standalone MySQL/MariaDB with tax and shipping fixtures; versioned adapters; end-user UX flows; performance and security/PII checks; release ZIP installation and upgrade. Tests cannot be green purely because they skipped all assertions. Every test produces a command, actual output, timestamp, environment metadata and link in `.ai/evidence-index.json`.

### 14.2 Required risky test catalogue (minimum, expand it)

- Free activates with WC, handles WC missing, Pro absent, Pro incompatible, Composer vendor missing; no fatal errors.
- Guest, allowed role context, invalid customer context, no data leaks, no session hijack.
- One simple product, variable product/variation, quantity update, virtual/downloadable, excluded/hidden catalog product, out-of-stock; clean restore after run.
- Coupon existence, min/max spend, expired coupon, usage limits, per-user cap, individual use, sale item restriction, product/category exclusion, free shipping flag, percent/fixed-cart/fixed-product coupon, multi-coupon stacking, vendor-filter rejection, unrecognized coupon.
- Compare coupon eligible base before and after other price changes; don't invent reasons.
- Shipping country/state/postcode, no rates, rate unavailable, package splitting, free-shipping threshold, local pickup, shipping classes, shipping tax, carrier API unavailable; block/cart variance.
- Tax inclusive/exclusive, exempt customer, compound, mixed classes, locale and currency precision, 0-decimal, arbitrary decimal rounding, fees taxable/non-taxable.
- Cart grand total overridden by hook; show unexplained delta; never fake fee.
- Two pricing extensions, duplicate-looking fees, no-op registered callbacks, unknown plugin intervention, verified adapter rule event, unsupported version, adapter absent.
- Trace max events/time exceeded, partial results, redaction and safe link to settings.
- Saved scenario missing product/variation, changed product price, changed WC settings, plugin versions, different currency, two runs, same/different inputs, copied/archived/deleted.
- Batch canceled/resumed, idempotent retry, timeouts, persistent queue failed job, no live checkout action.
- Permissions for each REST route/UI/export; CSRF, XSS, SQLi, CSV spreadsheet injection, path traversal, export data disclosure and retention.
- Confirm scenario run does not create order, decrement stock, consume coupon usage, send email or alter active admin/customer cart state in supported safe mode. Unknown vendor behavior must be explicitly isolated/staged and documented.
- Cart/Checkout Blocks and Classic checkout consistency on test fixture; don't claim total equivalence for unsupported third-party plugins.
- Free and Pro both optimized production ZIPs; portable to clean environments; no missing autoload; no dev dependencies.

See companion `docs/ACCEPTANCE_TEST_MATRIX.md` for individually numbered cases. Release criteria are stricter than a superficial count.

### 14.3 Definition of done per task

Real implementation exists; UI control works where applicable; dependency and security checks pass; tests assert actual behavior and retain evidence; docs and task status updated; no contradictory source of truth; compatibility claim reconciled; commit hash linked. `SKIPPED` without justification is not done. If environment lacks vendor paid integration, task remains blocked/limited with explicit product-claim exclusion; continue other development.

### 14.4 Release STOP conditions

Any untruthful rule attribution; leakage of customer PII/secrets; production checkout mutation; coupon usage/stock/order side effects in claimed safe mode; unbounded event collection; missing Free or Pro independent autoload; critical PHP fatal; broken role permissions; missing source evidence; unverified integration marketed as verified; broken tests in supported environment. Stop external release action, **not** unrelated safe development.

---

## 15. WORDPRESS PLAYGROUND & REPRODUCIBLE BLUEPRINT TESTING

### 15.1 Bundled blueprint profiles

Commit valid JSON Blueprints:

- `base/blueprint.json`: clean WordPress + WooCommerce, diagnostic admin login, no WPEssential source; baseline smoke.
- `free/blueprint.json`: WooCommerce + locally built Free plugin.
- `pro/blueprint.json`: WooCommerce + Free + separate Pro plugin.
- `compatibility/blueprint.json`: Free + Pro and only publicly installable explicitly verified compatible fixture plugins; placeholder profile must not pretend vendor integrations are installed.

Build actual `.zip` Blueprint bundles containing root `blueprint.json` and *existing, tested installable* plugin ZIPs as `resource:"bundled", path:"/slug.zip"`. `installPlugin` must use `pluginData` and activation options per current schema. Never create fake plugin artifacts to satisfy a Blueprint. If missing binaries, builder exits nonzero with explanatory error. Verify local JSON schema; a schema check is not runtime smoke. Official documentation currently describes bundled resources and plugin install steps; recheck at implementation time.

### 15.2 Runtime testing layers

Use WordPress Playground CLI/browser for quick smoke/UX and deterministic fixtures, plus WordPress/MySQL/MariaDB for real storage, concurrency and plugin compatibility; SQLite-based Playground cannot certify MySQL-specific constraints or side-effect safety for arbitrary vendor plugins. Put screenshot/video and test logs in `evidence/playground/` with verified times and environment. No claim `Playground passed` until actually run. Blueprint test fixture products may be created in disposable environments, never live.

### 15.3 Build and tool validation

Companion `scripts/build_playground_bundles.py` creates bundles after real Free/Pro ZIPs exist. `scripts/validate_blueprints.py` checks structure/local references. Check official Blueprint data format at runtime; do not use obsolete `pluginZipFile` forms. Include explicit failure tests for missing ZIP or broken autoload file. Documents explain how to run bundles locally and in browser if publicly hosted with direct resources/CORS.

---

## 16. DOCUMENTATION GENERATOR, README RULES AND VERSION HYGIENE

### 16.1 Single verified manifest

`templates/release/product-docs.example.json` is an intentionally **not release-approved** template. Implement release metadata as canonical, validate version/platform/commit/test IDs/feature tier, and derive *Free `readme.txt`, Free `README.md`, Pro `README.md`* from verified features only. Main plugin headers, `Stable tag`, changelog and supported PHP/WP/WC versions must agree. Missing evidence blocks generation; never invent tests or release approval. Translator `Text Domain`, domain path, action/filter docs, licensing and privacy notices consistent.

### 16.2 WordPress.org readme.txt

Must include directory-compatible header, short description within accepted length, Description, Installation, FAQ, Screenshots, Changelog, Upgrade Notice if applicable, License; WordPress core/requirements header truthfulness. Free-only features in directory description, never market unsupported Pro functions as free. No private telemetry. Run official WordPress readme validator/Plugin Check where access available; record actual results. Remember current WP directory plugin runtime minimum requirements are parsed from plugin main PHP header, not readme alone.

### 16.3 Documentation artifacts

`docs/USER_GUIDE.md`, `docs/ADMIN_GUIDE.md`, `docs/DEVELOPER_GUIDE.md`, `docs/ADAPTER_SDK.md`, `docs/TRACE_EVIDENCE_LEVELS.md`, `docs/SAFE_EXECUTION_AND_LIMITATIONS.md`, `docs/SCENARIO_JSON_SCHEMA.md`, `docs/COMPATIBILITY_MATRIX.md`, `docs/TEST_FIXTURES.md`, `docs/PRIVACY.md`, `docs/TROUBLESHOOTING.md`, `docs/CHANGELOG.md`, `docs/MARKETPLACE_SUBMISSION_FREE.md`, `docs/MARKETPLACE_SUBMISSION_PRO.md`, `docs/RELEASE_EVIDENCE.md`. Add accurate screenshots of implemented UI, not invented screenshots. Support and uninstall instructions must describe data retention and differences Free/Pro.

---

## 17. MARKETPLACE SUBMISSION CONTRACTS

### 17.1 WordPress.org — FREE

Use plugin name/slug and final package structure; Plugin Check, GPL compatibility, direct-include restriction and WordPress coding/security standards, no hidden paid obfuscation, no Pro features presented as available for Free, privacy and real usage documentation, translations, `readme.txt` and screenshots, build reproducibility, plugin activation smoke, vulnerability/security findings resolved. Record vendor account/logins as EXTERNAL gate. No submission claims without actual submission receipts.

### 17.2 WooCommerce Marketplace — PRO

Pro separately installable, Free dependency explained, complete reviewer instructions and scenarios, supported WP/WC/PHP requirements tested, HPOS compatibility declared only if applicable/validated, Cart/Checkout Blocks tested and accurately reported, QIT checks including activation, API, E2E, security, compatibility, malware and validation as official tooling permits. UI/UX and accessibility reviewed, common-extension conflicts tested, valid license/upgrade/update model and no unauthorized marketplace account use. Marketplace vendor approval and business review are external; prepare files/evidence but do not submit or accept terms without authorization. If marketplace freemium submission policy requires separate Free/paid submissions, document actual current rule and plan appropriately.

### 17.3 Reproducible release pipeline

`lint → static analysis → php unit → Woo integration → adapter tests → REST security → browser E2E → Playground smoke → MySQL concurrency/side effects → Plugin Check → QIT (where authorized) → docs generator → Composer optimized ZIPs → ZIP structural audit/checksums → reviewer evidence`. When a gate fails, fix and rerun affected suites; never bypass by writing a fabricated pass. Final artifacts include complete logs, version manifest, supported adapter versions and list of untested external integrations.

---

## 18. EXACT STARTING POINT AND FINAL COMMAND

1. Read Master and START AGENT IN FULL.
2. List repository contents and inspect source, git status and latest commits.
3. Recover actual `.ai/state.json`/`.ai/tasks.json`; initialize only when missing, without overwriting prior progress.
4. Determine exact phase and next dependency-unblocked task. If empty project, begin P0 with environment and WooCommerce API verification, then proof of safe admin diagnostic run.
5. Implement and test source code, create evidence, update memory, commit if allowed, and select the next task without asking for permission.
6. Continue through P1 Free, P2 Pro, P3 QA, P4 release readiness automatically **while the agent runtime is active**, honoring safety/permission boundaries.
7. At milestones, report completed task IDs, exact test evidence, blockers and current next task **while continuing** if runtime allows.
8. At any shutdown/context limit, checkpoint `START_HERE.md` and `.ai/state.json` accurately, ready for instant resumption.

**START EXECUTING. THIS CONTRACT IS NOT FULFILLED BY PLANNING ALONE.**

---

## 19. COMPANION IMPLEMENTATION SEEDS AND MACHINE-READABLE NEXT TASK

The companion package includes initial `.ai/tasks.template.json`, `.ai/state.template.json`, `docs/REQUIREMENTS_REGISTRY.json`, `docs/UI_SCREEN_INVENTORY.json`, `docs/ACCEPTANCE_TEST_MATRIX.md` and operational `scripts/agent_state.py`. Templates do not imply tasks have been executed.

From repository root after copying companion files to their intended paths:

```bash
python scripts/agent_state.py init
python scripts/agent_state.py next
python scripts/agent_state.py start P0-001
# implement task, run real tests and commit; write truthful JSON evidence
python scripts/agent_state.py complete P0-001 --commit ACTUAL_COMMIT_HASH --evidence path/to/actual-test-evidence.json
python scripts/agent_state.py next
```

The `complete` command MUST reject missing evidence, unmatched task IDs, missing required test IDs, absent execution environment/command/timestamp and uncommitted/unverified work. An automated code agent still needs to execute source changes and tests; the helper manages state, not background coding. Each completion updates the next-task pointer and `START_HERE.md`. The agent should immediately continue to the next task while its runtime is active; no human “continue” prompt. Read `PACKAGE_README.md` for setup and use `scripts/validate_blueprints.py` for Blueprint structural checks.

**Contract unchanged: Five phases only, no fake rule attribution, no untested compatibility claims, no permission-bypassing release actions.**
