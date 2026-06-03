<?php
/**
 * Tag logged-in WordPress users as internal GA4 traffic.
 *
 * Where this goes:
 *   - Child theme's functions.php, OR
 *   - A code-snippets plugin (e.g. "Code Snippets" by WPCode) — preferred,
 *     so a theme update can't silently erase it.
 *
 * What it does:
 *   Pushes traffic_type=internal for logged-in users (DSP staff) and
 *   traffic_type=external for everyone else, BEFORE GTM/Site Kit fire
 *   (priority 1 on wp_head). GTM reads dlv.traffic_type and forwards it to
 *   GA4 as an event parameter; GA4's Internal Traffic data filter then drops
 *   the internal hits.
 *
 * Pair with:
 *   - GTM: Data Layer Variable `dlv.traffic_type` -> GA4 tag field
 *     `traffic_type = {{dlv.traffic_type}}`.
 *   - GA4: custom dimension `traffic_type` (event-scoped) + Internal Traffic
 *     data filter (Testing, then Active).
 *
 * See denver-streets-audit.md §2d-quater.
 */

add_action('wp_head', function () {
    $traffic_type = is_user_logged_in() ? 'internal' : 'external';
    printf(
        "<script>window.dataLayer = window.dataLayer || [];"
        . "dataLayer.push({'traffic_type':'%s'});</script>\n",
        esc_js($traffic_type)
    );
}, 1); // priority 1 = emit before GTM container / Site Kit gtag loads
