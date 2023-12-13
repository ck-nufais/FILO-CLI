import os
import shutil

data = {
    "Web": [".html5", ".html", ".htm", ".xhtml"],
    "Picture": [
        ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
        ".heif", ".psd"
    ],
    "Video": [
        ".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
        ".mng", ".qt", ".mpg", ".mpeg", ".3gp"
    ],
    "Document": [
        ".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf",
        ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
        ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"
    ],
    "Compressed": [
        ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg",
        ".rar", ".xar", ".zip"
    ],
    "Audio": [
        ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv",
        "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
    ],
    "python": [".py"]
}


class Filo:

  def __init__(self,
               path: str = os.getcwd(),
               dest: str = os.getcwd(),
               data: dict = data,
               ignore: list = []) -> None:

    self.ignore = ignore
    self.computed = {
        value.lower(): key
        for key, values in data.items() for value in values
    }
    self.src = path
    self.dest = dest


  def CopyOperation(self, dest, src, filename):
    if not os.path.exists(dest):
      os.mkdir(dest)
    shutil.copyfile(src, (os.path.join(dest, filename)))


  def OrganiseDir(self):
    nonTouched = []
    for each in os.scandir(self.src):
      if each.is_file():
        list = os.path.splitext(each)
        ext = list[1].lower()
        filename = each.name
        if (ext in self.computed) and filename not in self.ignore:
          self.CopyOperation(os.path.join(self.dest, self.computed[ext]),
                                 each.path, filename)
        else:
          nonTouched.append(ext)
    return nonTouched



if __name__ == "__main__":
    test = Filo()
    test.OrganiseDir()

