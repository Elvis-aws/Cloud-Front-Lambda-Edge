import datetime

# The generated page contains some dynamic data, so we don't want
# it to stay in cache for long
cache_control_max_age = 3  # in seconds


def handler(event, context):
    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    html = "<html><title>Content generated by Lambda@Edge</title><body><h1>This content is generated by Lambda@Edge.</h1> <h3>Content generated at {}</h3></body></html>".format(
        date_time)

    response = {
        'status': 200,
        'headers': {
            "cache-control": [{"key": "Cache-Control", "value": "max-age={}".format(date_time)}],
            "content-type": [{"key": "Content-Type", "value": 'text/html;charset=UTF-8'}]
        },
        'body': html
    }

    return response
