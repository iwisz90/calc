import wx

class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title = title, size = (600, 800))

        self.Show()
        self.setup()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        self.textbox = wx.TextCtrl(self, style == wx.TE_RIGHT)
        box.Add(self.textbox, flag = wx.EXPAND | wx.TOP | wx.BOTTOM, border = 4)

        grid = wx.GridSizer(5, 4, 10, 10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        for label in buttons:
            button = wx.Button(self, -1, label)
            grid.Add(button, 0 , wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

        # grid.AddMany([
        #     (wx.Button(self, label = '7'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '8'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '9'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '/'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '4'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '5'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '6'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '*'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '1'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '2'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '3'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '-'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '0'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '.'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '+'), 0, wx.EXPAND),
        #     (wx.Button(self, label = '+'), 0, wx.EXPAND)
        # ])

        box.Add(grid, proportion = 1, flag = wx.EXPAND)
        self.SetSizer(box)

    def on_button_press(self, e):

        label = e.GetEventObject().GetLabel()

        calculation = self.textbox.GetValue()

        if label == '=':
            if not calculation:
                return

            result = eval(calculation)

            self.textbox.SetValue



if __name__ == '__main__':
    app = wx.App()
    Interface(None, title = 'Calculator')

app.MainLoop()