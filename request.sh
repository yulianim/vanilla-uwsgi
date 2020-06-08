curl -i --header "Content-Type: application/json" \
  --request POST \
  --data '{userId:"juan-perez-id-001", "time": "Fri Jun  5 21:00:24 CDT 2020", "lat":"10", "long":"20"}' \
http://localhost:9090/uwsgi-server/location
