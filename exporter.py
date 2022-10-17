#!/usr/bin/env python

from os import path, system
from random import randint

import inkex
from _io import BufferedWriter
from inkex.base import TempDirMixin
from inkex.command import take_snapshot


class CMYKExporter(TempDirMixin, inkex.OutputExtension):
    def set_extension(self, ext: str):
        self.file_ext = ext

    def save(self, stream: BufferedWriter):
        # Salva um arquivo temporário em SVG(formato mais rápido)
        tmpInput = take_snapshot(
            svg=self.document,
            dirname=self.tempdir,
            ext='svg'
        )
        tmpOutput = path.join(self.tempdir, f"{randint(1, 1000)}.{self.file_ext}")
        icc = path.join(self.ext_path(), "USWebCoatedSWOP.icc")
        # Chama o programa de conversão passando o SVG como entrada
        system(f"convert '{tmpInput}' -profile '{icc}' -colorspace CMYK '{tmpOutput}'")
        with open(tmpOutput, mode='rb') as output:
            stream.write(output.read())
