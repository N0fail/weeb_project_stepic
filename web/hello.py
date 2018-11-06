def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = env["QUERY_STRING"].split("&")
    res = []
    for key in body:
        key += "\r\n"
	res += [key]
    return res

