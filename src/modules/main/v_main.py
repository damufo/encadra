# -*- coding: utf-8 -*-


import wx
from wx import adv
from wx.lib.wordwrap import wordwrap
from modules.main.w_main import Main
from classes.wxp.view_plus import ViewPlus
from classes.wxp.messages import Messages


class View(Main):

    def __init__(self, presenter):
        Main.__init__(self, None)
        self.SetName('main')
        self.view_plus = ViewPlus(self)
        self.msg = Messages(self)
        self.picture = None
        self.force_fit = False
        self.on_size_enabled = True
        self.scroll_win.ShowScrollbars(
                horz=wx.SHOW_SB_NEVER,
                vert=wx.SHOW_SB_NEVER)

    def load_picture(self):
        if self.picture:
            bitmap = self.picture.bitmap
            self.sbx_picture.SetBitmap(bitmap)
            self.set_bottom_bar()
            self.Refresh()
            self.Layout()
        else:
            bitmap = wx.EmptyBitmapRGBA(1, 1, alpha=0)
            self.sbx_picture.SetBitmap(bitmap)
            self.status_bar.SetStatusText("")
            self.Layout()
            self.Refresh()

    def set_bottom_bar(self):
        picture_info = _("[{} of {}] {}{}  {}  {}  {}%").format(
            self.picture.pos + 1,
            len(self.picture.pictures),
            self.picture.modified and "*" or "",
            self.picture.file_name,
            self.picture.size_px,
            str(self.picture.size_bytes_h),
            str(int(self.picture.factor)))
        self.lbl_properties.SetLabel(picture_info)

    def get_picture_frame_size(self):
        size_to_fit = None
        border = 0
        size_to_fit = (
            self.scroll_win.Size.Width-border,
            self.scroll_win.Size.Height-border)
        return size_to_fit

    def draw_rectangle(self, rectangle):
        bitmap = self.picture.bitmap
        dc = wx.MemoryDC(bitmap)
        dc.SetPen(wx.Pen(colour="grey", width= 5, style=wx.SOLID))
        dc.SetBrush(wx.Brush("grey", wx.TRANSPARENT))
        dc.DrawRectangle(rectangle)
        dc.SelectObject(wx.NullBitmap)
        self.sbx_picture.SetBitmap(bitmap)
        self.scroll_win.Refresh()

    def about(self, config):
        info = adv.AboutDialogInfo()
        info.SetName(config.app_name)
        info.SetVersion(config.app_version)
        info.SetDescription(
            wordwrap(
                config.app_description,
                500,
                dc=wx.ClientDC(self.panel), breakLongWords=False))
        info.SetCopyright(config.app_copyright)
        info.SetWebSite(
            config.app_web_site,
            _("{} website".format(config.app_name)))
        info.AddDeveloper(config.app_developer)
        info.AddTranslator(config.app_developer)
        info.License = wordwrap(config.app_license, 500,
                                wx.ClientDC(self.panel))

        info.SetIcon(self.view_plus.app_icon)
        adv.AboutBox(info=info, parent=self)
