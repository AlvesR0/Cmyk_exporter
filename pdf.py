import exporter

exp = exporter.CMYKExporter()
exp.set_extension('pdf')
exp.run()
