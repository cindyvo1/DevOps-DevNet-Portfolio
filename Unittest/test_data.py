key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
    "version": 3,
    "id": "c0d37fc6-18f0-46ff-8d31-810781e68f99",
    "title": "Controller Issue",
    "issueDetails": {
        "severity": 2,
        "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
        "issueDescription": "The listed devices are unreachable from the controller",
        "resolutionLink": "http://www.cisco.com"
    },
    "devices": [
        {
            "serial": "FDO21171T7H",
            "hostname": "switch1",
            "status": "unreachable"
        },
        {
            "serial": "FDO21171T8A",
            "hostname": "switch2",
            "status": "unreachable"
        }
    ]
}
