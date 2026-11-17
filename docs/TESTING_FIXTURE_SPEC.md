# Test fixture contract — only for disposable isolated WooCommerce installations

No test below is evidence of a run. At P0 implement deterministic fixture seeding with item/product references and expected outcomes, then verify against supported WooCommerce versions. Never seed into production without explicit authorization.

## Fixture catalog

- Simple product A: USD 100, taxable standard, shipping required, stock 100.
- Simple product B: USD 80, taxable reduced-class, shipping required, stock 50.
- Virtual product C: USD 40, no shipping, standard tax where applicable.
- Variable T-shirt D: size S/M and color Black/White; variations have distinct price/stock and only expected combinations.
- Sale item E: regular USD 120, sale USD 90.
- Coupon FIX10: fixed-cart USD 10, suitable usage limits and clear restrictions.
- Coupon SAVE10: percentage 10%, no product exclusions.
- Coupon MIN100: threshold USD 100, to test eligibility before/after price adjustments.
- Coupon SALEEX: exclude sale items.
- Coupon FREESHIP: free-shipping eligible under official Woo settings.
- Tax rates: standard 10%, reduced 5% as *synthetic* values, not legal claims; also 0%, compound and tax-inclusive fixture.
- Shipping: zone US, Flat Rate USD 12, Local Pickup USD 0, Free Shipping threshold USD 100, second package configuration.
- Test context: Guest default, fictional wholesale role and fictional customer account with no real personal data.

## Diagnostic assertions

- A 2 × USD 100 product setup with a verified 10% price adjustment and a verified 10% coupon can yield item taxable base USD 162, tax USD 16.20, shipping USD 12 and non-taxable fee USD 5, total USD 195.20 **only under those synthetic assumptions**; do not hardcode this into engine calculations.
- Run with two pricing callbacks: no-op callback presence must not be attributed as cause of a price change.
- Run with direct final total override: show nonzero unexplained delta rather than inventing a fee.
- Simulate coupon failure and assert core usage counts did not change.
- Simulate safe diagnostic run and assert stock, orders, emails, real customer carts unaffected.
- Simulate unknown outbound carrier callback only in isolated/blocked-network staging profile; report limits.

## Seed execution protocol

Fixture scripts must be idempotent, request confirmation before destructive cleanup, use WC APIs for products and coupon definitions, and capture exact expected/actual amounts with WooCommerce environment/version. Coupon/tax rounding behavior may change by version: record evidence rather than expecting all environments to produce identical values.
