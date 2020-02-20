import csv
import os


conceptTemplate = ('@prefix skos:  <http://www.w3.org/2004/02/skos/core#> . \n'
                   '@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .\n\n'
                   '<{d}-{c}-{n}> a skos:Concept \n'
                   '\trdfs:label "{label}"@en \n'
                   '\t<http://metarelate.net/vocabulary/index.html#identifier> '
                   '\t<http://codes.wmo.int/def/common/edition> , '
                   '\t<http://codes.wmo.int/def/common/centre> , '
                   '\t<http://codes.wmo.int/def/grib2/discipline> , '
                   '\t<http://codes.wmo.int/def/grib2/parameter> , '
                   '\t<http://codes.wmo.int/def/grib2/category> ;\n'
                   '\t<http://codes.wmo.int/def/common/centre> <http://codes.wmo.int/common/centre/74> ;\n'
                   '\t<http://codes.wmo.int/def/common/edition> <http://codes.wmo.int/codeform/grib2> ;\n'
                   '\t<http://codes.wmo.int/def/common/unit> "{u}" ;\n'
                   '\t<http://codes.wmo.int/def/grib2/category> <http://codes.wmo.int/grib2/codeflag/4.1/{d}-{c}> ;\n'
                   '\t<http://codes.wmo.int/def/grib2/discipline> <http://codes.wmo.int/grib2/codeflag/0.0/{d}> ;\n'
                   '\t<http://codes.wmo.int/def/grib2/parameter> {n} ;\n'
                   '\tskos:related <http://reference.metoffice.gov.uk/um/stash/m01s{ss}i{si}>')

root_path = os.path.dirname(__file__)
with open(os.path.join([root_path, 'GRIB2LocalTable.csv'])) as cf:
    greader = csv.DictReader(cf)

    if not os.path.exists('mo--74'):
        os.mkdir('mo--74')
    for entity in greader:
        with open('mo--74/{d}-{c}-{n}.ttl'.format(d=entity['Discipline'],
                                                 c=entity['Category'],
                                                 n=entity['Number']), 'w') as fh:
            fh.write(conceptTemplate.format(d=entity['Discipline'],
                                            c=entity['Category'],
                                            n=entity['Number'],
                                            label=entity['Parameter'],
                                            u=entity['Unit'],
                                            ss=int(int(entity['STASH code'])/1000),
                                            si=int(entity['STASH code'])%1000))