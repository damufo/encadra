# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jun 11 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

# import gettext
# _ = gettext.gettext

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Encadra"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.panel.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.scroll_win = wx.ScrolledWindow( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scroll_win.SetScrollRate( 5, 5 )
		self.scroll_win.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.sbx_picture = wx.StaticBitmap( self.scroll_win, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.sbx_picture, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.scroll_win.SetSizer( bSizer1 )
		self.scroll_win.Layout()
		bSizer1.Fit( self.scroll_win )
		bSizer41.Add( self.scroll_win, 1, wx.EXPAND, 0 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.lbl_properties = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_properties.Wrap( -1 )

		self.lbl_properties.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.lbl_properties.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer5.Add( self.lbl_properties, 1, wx.EXPAND, 0 )


		bSizer41.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.panel.SetSizer( bSizer41 )
		self.panel.Layout()
		bSizer41.Fit( self.panel )
		bSizer4.Add( self.panel, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer4 )
		self.Layout()
		self.menu = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.mnu_open = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Open")+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_open )

		self.mnu_save = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Save")+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_save )

		self.mnu_save_as = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Save as...")+ u"\t" + u"CTRL+SHIFT+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_save_as )

		self.m_menu1.AppendSeparator()

		self.mnu_rename = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Rename")+ u"\t" + u"F2", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_rename )

		self.mnu_delete = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Delete")+ u"\t" + u"DELETE", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_delete )

		self.m_menu1.AppendSeparator()

		self.mnu_quit = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Quit")+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.mnu_quit )

		self.menu.Append( self.m_menu1, _(u"&File") )

		self.mnu_edit = wx.Menu()
		self.mnu_resize = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Resize")+ u"\t" + u"S", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_resize )

		self.mnu_autoresize = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Auto-resize")+ u"\t" + u"SHIFT+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_autoresize )

		self.mnu_crop = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Crop")+ u"\t" + u"C", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_crop )

		self.mnu_rotate_right = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Rotate right")+ u"\t" + u"R", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_rotate_right )

		self.mnu_rotate_left = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Rotate left")+ u"\t" + u"SHIFT+R", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_rotate_left )

		self.mnu_rotate_custom = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Rotate custom")+ u"\t" + u"A", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_rotate_custom )

		self.mnu_flip_h = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Flip horizontally")+ u"\t" + u"F", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_flip_h )

		self.mnu_flip_v = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Flip vertically")+ u"\t" + u"SHIFT+F", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_flip_v )

		self.mnu_edit.AppendSeparator()

		self.mnu_preferences = wx.MenuItem( self.mnu_edit, wx.ID_ANY, _(u"Preferences")+ u"\t" + u"CTRL+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_edit.Append( self.mnu_preferences )

		self.menu.Append( self.mnu_edit, _(u"&Edit") )

		self.mnu_view = wx.Menu()
		self.mnu_fullscreen = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Fullscreen")+ u"\t" + u"F11", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_fullscreen )

		self.mnu_view.AppendSeparator()

		self.mnu_go_next = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Go next")+ u"\t" + u"SPACE", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_go_next )

		self.mnu_go_prev = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Go previous")+ u"\t" + u"BACK", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_go_prev )

		self.mnu_go_first = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Go first")+ u"\t" + u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_go_first )

		self.mnu_go_last = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Go last")+ u"\t" + u"End", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_go_last )

		self.mnu_view.AppendSeparator()

		self.mnu_zoom_in = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Zoom in")+ u"\t" + u"+", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_zoom_in )

		self.mnu_zoom_out = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Zoom out")+ u"\t" + u"-", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_zoom_out )

		self.mnu_zoom_1 = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Zoom 100%")+ u"\t" + u"1", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_zoom_1 )

		self.mnu_zoom_fit = wx.MenuItem( self.mnu_view, wx.ID_ANY, _(u"Zoom fit")+ u"\t" + u"0", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_view.Append( self.mnu_zoom_fit )

		self.menu.Append( self.mnu_view, _(u"&View") )

		self.mnu_help = wx.Menu()
		self.mnu_homepage = wx.MenuItem( self.mnu_help, wx.ID_ANY, _(u"Homepage")+ u"\t" + u"CTRL+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_help.Append( self.mnu_homepage )

		self.mnu_report_bug = wx.MenuItem( self.mnu_help, wx.ID_ANY, _(u"Report a bug")+ u"\t" + u"CTRL+B", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_help.Append( self.mnu_report_bug )

		self.mnu_source = wx.MenuItem( self.mnu_help, wx.ID_ANY, _(u"Source")+ u"\t" + u"CTRL+U", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_help.Append( self.mnu_source )

		self.mnu_help.AppendSeparator()

		self.mnu_about = wx.MenuItem( self.mnu_help, wx.ID_ANY, _(u"About")+ u"\t" + u"CTRL+A", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_help.Append( self.mnu_about )

		self.menu.Append( self.mnu_help, _(u"&Help") )

		self.SetMenuBar( self.menu )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_resize, id = self.mnu_resize.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_resize( self, event ):
		event.Skip()


