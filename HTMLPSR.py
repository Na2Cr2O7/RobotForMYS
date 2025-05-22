
from datetime import datetime
def toHTMLStatus(List, title):
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    """
    for item in List:
        time=item[0].strftime("%Y-%m-%d %H:%M:%S")
        status=item[1]
        html_template += f"<p><b>{time}</b>  {status}</p>"

    html_template += f"""
</body>
</html>
    """
    return html_template
def toHTMLList(List, title):
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    """
    for i, item in enumerate(List):
        
        
        html_template += f"<p><b>{i+1}</b>  {item}</p>"

    html_template += f"""
</body>
</html>
    """

    return html_template
def toHTMLDict(dictionary, title):
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    """
    for key, value in dictionary.items():
        html_template += f"<p>{key} → <b>{value}</b> </p>"

    html_template += f"""
</body>
</html>
    """

    return html_template
def writeHTML(html, filename='0.html'):
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(html)
    return filename
def openinBrowser(filename):
    import webbrowser
    import os
    if not os.path.exists(filename):
        filename=writeHTML(filename)
    webbrowser.open_new_tab(filename)
if __name__ == '__main__':
    List = [
        (datetime.now(), "Status 1"),
        (datetime.now(), "Status 2"),
        (datetime.now(), "Status 3"),
    ]
    title = "Status Viewer"
    html = toHTMLStatus(List, title)
    with open("status.html", "w") as f:
        f.write(html)