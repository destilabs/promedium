def get_element_by_selector(html, selector):
    elem = html.select(selector)

    if len(elem) > 0:
        return next(iter(elem)).getText().replace('\n',' ').strip()
    else: 
        print(f'Missing value for selector {selector}')
        return ''