import zip_processor, zip_replace, scale_zip


# test zip replace
zip_processor = zip_processor.ZipProcessor(zip_replace.ZipReplace("Mexico", "Ua"), "test_replace.zip")
zip_processor.process_zip()

# test scale zip
zip_processor = zip_processor.ZipProcessor(scale_zip.ScaleZip(), "test_im.zip")
zip_processor.process_zip(1200, 400)
