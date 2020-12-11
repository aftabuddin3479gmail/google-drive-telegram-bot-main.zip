from pyrogram import Client, filters
from bot.config import BotCommands, Messages
from bot.helpers.utils import CustomFilters
from bot.helpers.gdrive_utils import GoogleDrive
from bot import LOGGER

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Clone) & CustomFilters.auth_users)
def _clone(client, message):
  user_id = message.from_user.id
  if len(message.command) > 1:
    link = message.command[1]
    LOGGER.info(f'Copy:{user_id}: {link}')
    sent_message = message.reply_text(Messages.CLONING.format(link), quote=True)
    msg = GoogleDrive(user_id).clone(link)
    sent_message.edit(msg)

    from bot.fs_utils import get_readable_file_size

class DownloadStatus:
    def __init__(self, size=0):
            self.size = size
                    self.name = ''
                            self.status = False
                                    self.checking = False
                                            self.MainFolderName = ''
                                                    self.MainFolderLink = ''
                                                            self.DestinationFolderName = ''
                                                                    self.DestinationFolderLink = ''

    def get_size(self):
            return get_readable_file_size(int(self.size))
    def add_size(self, value):
            self.size += int(value)
    def set_name(self, name=''):
            self.name = name
    def get_name(self):
            return self.name
    def set_status(self, stat):
            self.status = stat
    def done(self):
            return self.status
    def checkFileExist(self, checking=False):
            self.checking = checking
    def checkFileStatus(self):
            return self.checking
    def SetMainFolder(self, folder_name, link):
            self.MainFolderName = folder_name
                    self.MainFolderLink = link
    def SetDestinationFolder(self, folder_name, link):
            self.DestinationFolderName = folder_name
                    self.DestinationFolderLink = link

  else:
    message.reply_text(Messages.PROVIDE_GDRIVE_URL.format(BotCommands.Clone[0]))
