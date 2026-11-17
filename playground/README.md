# WordPress Playground — Cart Rules Inspector

These are **templates**, not claims of successful runtime execution. The `base` profile installs WooCommerce; `free` adds the real Free plugin; `pro` installs both Free and Pro; `compatibility` adds AlgolPlus Advanced Dynamic Pricing as a **candidate unverified integration under test**, not a claim of verified support. Disable outbound integrations/test with disposable fixtures.

```bash
python scripts/validate_blueprints.py
python scripts/build_playground_bundles.py --base-only --out dist/playground
```

After build of actual, separately installable and Composer-vendored plugins:

```bash
python scripts/build_playground_bundles.py --free dist/wpessential-cart-rules-inspector.zip --pro dist/wpessential-cart-rules-inspector-pro.zip --out dist/playground
```

The output bundles contain root `blueprint.json` plus actual plugin ZIP resources. Test with official WordPress Playground tooling; check current CLI command flags/version at runtime. Example command patterns may vary by CLI version:

```bash
npx @wp-playground/cli server --blueprint=dist/playground/free-playground-bundle.zip
npx @wp-playground/cli server --blueprint=dist/playground/pro-playground-bundle.zip
```

Do not claim Playground passed based on JSON checks or bundle packaging alone. Capture actual screen, WC calculation, and plugin side-effect test evidence. Playground SQLite is not a substitute for real MySQL/MariaDB/WooCommerce integration tests.

Official reference: https://wordpress.github.io/wordpress-playground/blueprints/bundles/
