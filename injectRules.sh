# rules for S1, S2, S3, S4 are the same
for i in $(seq 1 4); do
 for j in $( seq 2 4); do 
  curl -X POST -d '{"match": {"ip_dscp":  "0", "in_port": "'$j'"}, "actions":{"queue": "1"}}' http://localhost:8080/qos/rules/000000000000000$i
  curl -X POST -d '{"match": {"ip_dscp": "10", "in_port": "'$j'"}, "actions":{"queue": "3"}}' http://localhost:8080/qos/rules/000000000000000$i
  curl -X POST -d '{"match": {"ip_dscp": "12", "in_port": "'$j'"}, "actions":{"queue": "2"}}' http://localhost:8080/qos/rules/000000000000000$i
 done
done


# rules and meter table for switch S3 to S13
curl -X POST -d '{"match": {"nw_src":"10.0.0.1/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000005
curl -X POST -d '{"match": {"nw_src":"10.0.0.2/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000005
curl -X POST -d '{"match": {"nw_src":"10.0.0.3/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000005
curl -X POST -d '{"meter_id": "1", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "300", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000005



curl -X POST -d '{"match": {"nw_src":"10.0.0.4/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000006
curl -X POST -d '{"match": {"nw_src":"10.0.0.5/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000006
curl -X POST -d '{"match": {"nw_src":"10.0.0.6/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000006
curl -X POST -d '{"meter_id": "1", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "400", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000006


curl -X POST -d '{"match": {"nw_src":"10.0.0.7/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000007
curl -X POST -d '{"match": {"nw_src":"10.0.0.8/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000007
curl -X POST -d '{"match": {"nw_src":"10.0.0.9/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000007
curl -X POST -d '{"meter_id": "3", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "500", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000007


curl -X POST -d '{"match": {"nw_src":"10.0.0.10/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000008
curl -X POST -d '{"match": {"nw_src":"10.0.0.11/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000008
curl -X POST -d '{"match": {"nw_src":"10.0.0.12/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000008
curl -X POST -d '{"meter_id": "1", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "300", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000008



curl -X POST -d '{"match": {"nw_src":"10.0.0.13/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000009
curl -X POST -d '{"match": {"nw_src":"10.0.0.14/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000009
curl -X POST -d '{"match": {"nw_src":"10.0.0.15/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000009
curl -X POST -d '{"meter_id": "2", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "400", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000009


curl -X POST -d '{"match": {"nw_src":"10.0.0.16/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000010
curl -X POST -d '{"match": {"nw_src":"10.0.0.17/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000010
curl -X POST -d '{"match": {"nw_src":"10.0.0.18/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000010
curl -X POST -d '{"meter_id": "3", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "500", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000010


curl -X POST -d '{"match": {"nw_src":"10.0.0.19/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000011
curl -X POST -d '{"match": {"nw_src":"10.0.0.20/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000011
curl -X POST -d '{"match": {"nw_src":"10.0.0.21/32"}, "actions":{"mark":"0", "meter": "1"}}' http://localhost:8080/qos/rules/0000000000000011
curl -X POST -d '{"meter_id": "1", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "300", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000011


curl -X POST -d '{"match": {"nw_src":"10.0.0.22/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000012
curl -X POST -d '{"match": {"nw_src":"10.0.0.23/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000012
curl -X POST -d '{"match": {"nw_src":"10.0.0.24/32"}, "actions":{"mark":"12", "meter": "2"}}' http://localhost:8080/qos/rules/0000000000000012
curl -X POST -d '{"meter_id": "2", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "400", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000012

curl -X POST -d '{"match": {"nw_src":"10.0.0.25/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000013
curl -X POST -d '{"match": {"nw_src":"10.0.0.26/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000013
curl -X POST -d '{"match": {"nw_src":"10.0.0.27/32"}, "actions":{"mark":"10", "meter": "3"}}' http://localhost:8080/qos/rules/0000000000000013
curl -X POST -d '{"meter_id": "3", "flags": "KBPS", "bands"  :[{"type":"DSCP_REMARK", "rate": "500", "prec_level": "1"}]}' http://localhost:8080/qos/meter/0000000000000013
