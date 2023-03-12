import ROOT as r

def set_pave_position(pave, x1, y1, x2, y2):
    pave.SetX1NDC(x1)
    pave.SetY1NDC(y1)
    pave.SetX2NDC(x2)
    pave.SetY2NDC(y2)

def set_canvas_size(height, width):
    r.gStyle.SetCanvasDefH(height)  # default 500
    r.gStyle.SetCanvasDefW(width)   # default 700

def set_label(var, size_x, size_y, div_x=None, div_y=None):
    var.SetLabelSize(size_x, "X")
    var.SetLabelSize(size_y, "Y")
    if (div_x is not None):
        var.GetXaxis().SetNdivisions(div_x)
    if (div_y is not None):
        var.GetYaxis().SetNdivisions(div_y)

def set_marker(var, marker_style, marker_color, marker_size):
    var.SetMarkerStyle(marker_style)
    var.SetMarkerColor(marker_color)
    var.SetMarkerSize(marker_size)
    
def set_line(var, line_color, line_width):
    var.SetLineColor(line_color)
    var.SetLineWidth(line_width)
    
def set_titles(var, main_title="", x_title="", y_title="", x_size=None, y_size=None, 
               x_offset=None, y_offset=None):
    var.SetTitle(main_title)
    var.GetXaxis().SetTitle(x_title)
    var.GetYaxis().SetTitle(y_title)
    var.GetYaxis().CenterTitle(True)
    if (x_size is not None):
        var.GetXaxis().SetTitleSize(x_size)
    if (y_size is not None):
        var.GetYaxis().SetTitleSize(y_size)
    if (x_offset is not None):
        var.SetTitleOffset(x_offset, "X")
    if (y_offset is not None):
        var.SetTitleOffset(y_offset, "Y")