#Boa:Frame:Frame1

import wx
import wx.lib.hyperlink
import sqlite3
import CustomDlg
import func
import Frame2
from bottle import route, run,template
import thread
import webbrowser

HOST='localhost'
PORT="8081"
LOCALURL = u"http://"+HOST+":"+PORT

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNADD, wxID_FRAME1BTNDELETE, wxID_FRAME1BTNEDIT, 
 wxID_FRAME1BTNFIND, wxID_FRAME1BTNQUIT, wxID_FRAME1BTNSEEALLRECORDS, 
 wxID_FRAME1BTNSEERESUME, wxID_FRAME1PANEL1, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATUSBAR1, 
] = [wx.NewId() for _init_ctrls in range(12)]

[wxID_FRAME1MENUFILEADD, wxID_FRAME1MENUFILEDELETE, wxID_FRAME1MENUFILEEDIT, 
 wxID_FRAME1MENUFILEFIND, wxID_FRAME1MENUFILEQUIT, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(5)]

[wxID_FRAME1MENUHELPABOUT] = [wx.NewId() for _init_coll_menuHelp_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'File')
        parent.Append(menu=self.menuHelp, title=u'Help')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'A Python Student Database',
              id=wxID_FRAME1MENUHELPABOUT, kind=wx.ITEM_NORMAL, text=u'About')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAboutMenu,
              id=wxID_FRAME1MENUHELPABOUT)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Add a record', id=wxID_FRAME1MENUFILEADD,
              kind=wx.ITEM_NORMAL, text=u'Add Record')
        parent.Append(help=u'Delete a Record', id=wxID_FRAME1MENUFILEDELETE,
              kind=wx.ITEM_NORMAL, text=u'Delete Record')
        parent.Append(help=u'Find a Record', id=wxID_FRAME1MENUFILEFIND,
              kind=wx.ITEM_NORMAL, text=u'Find Record')
        parent.Append(help=u'Edit a Record', id=wxID_FRAME1MENUFILEEDIT,
              kind=wx.ITEM_NORMAL, text=u'Edit Record')
        parent.Append(help=u'Quit', id=wxID_FRAME1MENUFILEQUIT,
              kind=wx.ITEM_NORMAL, text=u'Quit')
        self.Bind(wx.EVT_MENU, self.OnMenuFileAddMenu,
              id=wxID_FRAME1MENUFILEADD)
        self.Bind(wx.EVT_MENU, self.OnMenuFileDeleteMenu,
              id=wxID_FRAME1MENUFILEDELETE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileFindMenu,
              id=wxID_FRAME1MENUFILEFIND)
        self.Bind(wx.EVT_MENU, self.OnMenuFileEditMenu,
              id=wxID_FRAME1MENUFILEEDIT)
        self.Bind(wx.EVT_MENU, self.OnMenuFileQuitMenu,
              id=wxID_FRAME1MENUFILEQUIT)

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title=u'File')

        self.menuHelp = wx.Menu(title=u'Help')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(677, 221), size=wx.Size(433, 313),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Student Database')
        self._init_utils()
        self.SetClientSize(wx.Size(433, 313))
        self.SetMenuBar(self.menuBar1)
        self.SetBackgroundColour(wx.Colour(165, 42, 42))
        self.SetIcon(wx.Icon(u'/home/ashmeet/resume.ico', wx.BITMAP_TYPE_ICO))
        self.SetIcon(wx.Icon(u'/home/ashmeet/python/student/resume.jpg',
              wx.BITMAP_TYPE_JPEG))
        self.SetIcon(wx.Icon(u'/home/ashmeet/python/student/resume.jpeg',
              wx.BITMAP_TYPE_JPEG))

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.SetStatusBar(self.statusBar1)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(433, 288),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(165, 42, 42))
        self.panel1.SetToolTipString(u'')

        self.btnDelete = wx.Button(id=wxID_FRAME1BTNDELETE,
              label=u'&Delete Record', name=u'btnDelete', parent=self.panel1,
              pos=wx.Point(10, 40), size=wx.Size(118, 29), style=0)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnDelete,
              id=wxID_FRAME1BTNDELETE)

        self.btnAdd = wx.Button(id=wxID_FRAME1BTNADD, label=u'&Add Record',
              name=u'btnAdd', parent=self.panel1, pos=wx.Point(148, 40),
              size=wx.Size(118, 29), style=0)
        self.btnAdd.Bind(wx.EVT_BUTTON, self.OnAdd, id=wxID_FRAME1BTNADD)

        self.btnFind = wx.Button(id=wxID_FRAME1BTNFIND, label=u'&Find Record',
              name=u'btnFind', parent=self.panel1, pos=wx.Point(286, 40),
              size=wx.Size(118, 29), style=0)
        self.btnFind.Bind(wx.EVT_BUTTON, self.OnFind, id=wxID_FRAME1BTNFIND)

        self.btnEdit = wx.Button(id=wxID_FRAME1BTNEDIT, label=u'&Edit Record',
              name=u'btnEdit', parent=self.panel1, pos=wx.Point(10, 92),
              size=wx.Size(118, 29), style=0)
        self.btnEdit.Bind(wx.EVT_BUTTON, self.OnEdit, id=wxID_FRAME1BTNEDIT)

        self.btnQuit = wx.Button(id=wxID_FRAME1BTNQUIT, label=u'&Quit',
              name=u'btnQuit', parent=self.panel1, pos=wx.Point(148, 92),
              size=wx.Size(118, 29), style=0)
        self.btnQuit.Bind(wx.EVT_BUTTON, self.OnQuit, id=wxID_FRAME1BTNQUIT)

        self.btnSeeResume = wx.Button(id=wxID_FRAME1BTNSEERESUME,
              label=u'&See Resume', name=u'btnSeeResume', parent=self.panel1,
              pos=wx.Point(286, 92), size=wx.Size(118, 29), style=0)
        self.btnSeeResume.Bind(wx.EVT_BUTTON, self.OnSeeResume,
              id=wxID_FRAME1BTNSEERESUME)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'RESUME', name='staticText1', parent=self.panel1,
              pos=wx.Point(150, 8), size=wx.Size(126, 32), style=0)
        self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, u'Sans'))
        self.staticText1.SetForegroundColour(wx.Colour(255, 255, 0))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'/home/ashmeet/python/student/index3.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(176, 168),
              size=wx.Size(120, 98), style=0)
        self.staticBitmap1.SetBackgroundColour(wx.Colour(191, 191, 191))
        self.staticBitmap1.SetToolTipString(u'')

        self.btnSeeAllRecords = wx.Button(id=wxID_FRAME1BTNSEEALLRECORDS,
              label=u'See All Records', name=u'btnSeeAllRecords',
              parent=self.panel1, pos=wx.Point(10, 144), size=wx.Size(118, 29),
              style=0)
        self.btnSeeAllRecords.Bind(wx.EVT_BUTTON, self.OnSeeAllRecords,
              id=wxID_FRAME1BTNSEEALLRECORDS)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.childFrame = Frame2.Frame2new(self)
       

    def OnDelete(self, event):
        func.OnDelete(self, event)

    def OnMenuFileAddMenu(self, event):
        func.OnMenuFileAddMenu(self, event)

    def OnMenuFileDeleteMenu(self, event):
        func.OnMenuFileDeleteMenu(self, event)

    def OnMenuHelpAboutMenu(self, event):
        event.Skip()

    def OnAdd(self, event):
        func.OnAdd(self, event)

    def OnMenuFileFindMenu(self, event):
        func.OnMenuFileFindMenu(self,event)

    def OnFind(self, event):
        func.OnFind(self, event)

    def OnMenuFileEditMenu(self, event):
        func.OnMenuFileEditMenu(self, event)

    def OnMenuFileQuitMenu(self, event):
        self.Close()

    def OnEdit(self, event):
        func.OnEdit(self, event)

    def OnQuit(self, event):
        self.Close()

    
    def OnSeeResume(self, event):
        func.OnSeeResume(self, event)

    def OnHyperLinkCtrl1Left(self, event):
        func.OnHyperLinkCtrl1Left(self, event)

    def OnSeeAllRecords(self, event):
        func.OnSeeAllRecords(self, event)

        
    


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()

#class WxApp(wx.App):
#    appFrame = None
#
#    def OnInit(self):
#        self.appFrame = Frame1()
#        self.appFrame.Show()
#        return True
#
#if __name__ == '__main__':
#    wxApp = WxApp(redirect=False)
#    wx.CallAfter(wxApp.appFrame.StartServer)
#    wxApp.MainLoop() 
