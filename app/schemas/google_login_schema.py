google_login_schema = {
    "type": "object",
    "properties": {
        "tokenId": {
            "type": "string",
            "pattern": r"^[\w-]*\.[\w-]*\.[\w-]*$"
        },
    },
    "required": [
        "tokenId"
    ],
    "additionalProperties": False
}
