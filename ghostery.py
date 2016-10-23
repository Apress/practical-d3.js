data = {
    'The Guardian': ["AppNexus", "DoubleClick", "eXelate", "Google Adsense", "Google AdWords Conversion", "Google Dynamic Remarketing", "Krux Digital", "LiveRamp", "NetRatings SiteCensus", "Rubicon", "ScoreCard Research Beacon", "VisualDNA"],
    'NYTimes': ["[x+1]", "AppNexus", "BidSwitch", "BrightRoll", "ChartBeat", "ClickTale", "DataXu", "DoubleClick", "DoubleClick Floodlight", "Dynamic Yield", "Ensighten", "Facebook Connect", "Facebook Custom Audience", "Google Adsense", "Google Analytics", "Index Exchange (Formerly Casale Media)", "LiveRail", "Moat", "NetRatings SiteCensus", "New Relic", "OpenX", "Optimizely", "PubMatic", "Quantcast", "Rocket Fuel", "Rubicon", "ScoreCard Research Beacon", "Tapad", "Twitter Advertising", "WebTrends"],
    'BBC': ["BidSwitch", "ChartBeat", "DoubleClick", "Effective Measure", "Flashtalking", "Ghostery Privacy Notice", "Google Adsense", "Google Analytics", "iPerceptions", "Krux Digital", "Rubicon", "ScoreCard Research Beacon", "Yieldr"],
    'Zeit': ["Adition", "DoubleClick", "DoubleClick Spotlight", "Google Adsense", "Google AdWords Conversion", "Google Analytics", "Google Dynamic Remarketing", "Google Tag Manager", "INFOnline", "Integral Ad Science", "Meetrics", "Nugg.Ad", "Semasio", "The ADEX", "Webtrekk", "xplosion", "Yieldlab"],
    'Volkskrant': ["AppNexus", "ChartBeat", "Datalogix", "DoubleClick", "DoubleClick Bid Manager", "eXelate", "Ghostery Privacy Notice", "Google Adsense", "Google Analytics", "Google Tag Manager", "Krux Digital", "Rubicon", "Usabilla", "VisualDNA", "Weborama", "Yieldr"],
}


def get_nodes(data):
    nodes = []
    plugins = []
    for newspaper in data:
        nodes.append({'name': newspaper, 'type': 'newspaper'})
        plugins.extend(data[newspaper])
    for plugin in set(plugins):
        nodes.append({'name': plugin, 'type': 'plugin'})
    return nodes

def get_links(data, nodes):
    links = []
    for i, s in enumerate(nodes):
        for j,t in enumerate(nodes):
            if s['type'] == 'newspaper' and t['type'] == 'plugin':
                if t['name'] in data[s['name']]:
                    links.append({'source': i, 'target': j})
    return links


if __name__ == '__main__':
    nodes = get_nodes(data)
    links = get_links(data, nodes)

    print nodes
    print links
