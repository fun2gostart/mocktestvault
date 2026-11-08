Deployment notes — MockTestVault v2.9.8 Academic Integration Candidate

1. Back up the current Hostinger public_html before deployment.
2. Upload the archive contents to the document root, preserving relative paths.
3. After deployment, verify /sw.js returns CACHE_NAME mtv-cbt-v47.
4. Test one practice page and all three sets for each chapter; verify JSON responses are HTTP 200.
5. Clear any host/CDN cache if stale question content is served. The service worker uses v47 and removes prior cache stores on activation.
6. Test exam start, answer selection, navigation, timer, submit/score, and mobile layout.
7. Check browser console and network requests for JSON errors.

This ZIP is a candidate. Human academic sign-off is still pending and the site has not been deployed or tested on Hostinger.
