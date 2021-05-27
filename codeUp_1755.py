file, extension = input().split('.')
"""
extension_dictionary = {
    dib: 'Paint.Picture',
    doc: 'Word.Document.8',  
    docx: 'Word.Document.12',  
    htm: 'htmfile',  
    html: 'htmlfile',  
    hwp: 'Hwp.Document.96',  
    hwpx: 'Hwp.Document.hwpx.96',  
    hwt: 'Hwp.Document.hwt.96',  
    jpe: 'jpegfile',
    jpeg: 'jpegfile',
    jpg : 'jpegfile',  
    ppt: 'PowerPoint.Show.8',
    pptx: 'PowerPoint.Show.12',
    pptxml: 'powerpointxmlfile'
}
"""

extension_list = dict(
    dib = 'Paint.Picture',
    doc = 'Word.Document.8',  
    docx = 'Word.Document.12',  
    htm = 'htmfile',  
    html = 'htmlfile',  
    hwp = 'Hwp.Document.96',  
    hwpx = 'Hwp.Document.hwpx.96',  
    hwt = 'Hwp.Document.hwt.96',  
    jpe = 'jpegfile',
    jpeg = 'jpegfile',
    jpg = 'jpegfile',  
    ppt = 'PowerPoint.Show.8',
    pptx = 'PowerPoint.Show.12',
    pptxml = 'powerpointxmlfile')

print(extension_list[extension])
