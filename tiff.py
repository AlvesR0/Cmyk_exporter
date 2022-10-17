import exporter

exp = exporter.CMYKExporter()
exp.set_extension('tiff')
exp.run()