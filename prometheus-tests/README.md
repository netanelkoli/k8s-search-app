# Prometheus Tests

Measuring the latency for the `search` endpoint.

## HOW-TO

1. Install the `serviceMonitor` CRD:
`kubectl apply -f https://raw.githubusercontent.com/│
prometheus-operator/prometheus-operator/v0.56.0/example/prometheus-operator-crd/monitoring.coreos.com_│
servicemonitors.yaml`
2. Apply the helm chart with the `serviceMonitor.yaml` template: `helm upgrade --install doc-search .`
3. Get the url for the doc-search app: `minikube service doc-search --url`
4. Generate some load using `./hey_linux_amd64 -z 2m http://<MINIKUBE_IP>:<SVC_PORT>/?q=hello+world`
5. 3. Go to the prometheus web UI: `minikube service doc-search-prometheus-server --url`
6. Run the following query: `http://<MINIKUBE_IP>:<SVC_PORT>/graph?g0.expr=histogram_quantile(0.95%2C%20sum(rate(flask_http_request_duration_seconds_bucket%5B5m%5D))%20by%20(le))&g0.tab=0&g0.stacked=0&g0.show_exemplars=0&g0.range_input=15m&g1.expr=histogram_quantile(0.50%2C%20sum(rate(flask_http_request_duration_seconds_bucket%5B5m%5D))%20by%20(le))&g1.tab=0&g1.stacked=0&g1.show_exemplars=0&g1.range_input=15m&g2.expr=histogram_quantile(0.99%2C%20sum(rate(flask_http_request_duration_seconds_bucket%5B5m%5D))%20by%20(le))&g2.tab=0&g2.stacked=0&g2.show_exemplars=0&g2.range_input=15m`
