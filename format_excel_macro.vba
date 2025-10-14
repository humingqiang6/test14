Sub FormatExcelSheet()
    '
    ' FormatExcelSheet Macro
    ' This macro formats the active Excel sheet with a title, bold headers, and auto-fits columns.
    '

    ' Add a title in cell A1 and merge it across the first 5 columns
    With Range("A1:E1")
        .Value = "Formatted Data Report"
        .Font.Bold = True
        .Font.Size = 14
        .HorizontalAlignment = xlCenter
        .Merge
    End With

    ' Assume headers are in row 2, format them as bold
    Dim HeaderRange As Range
    Set HeaderRange = Range("A2").CurrentRegion.Rows(1) ' This finds the header row based on data
    HeaderRange.Font.Bold = True
    HeaderRange.Interior.Color = RGB(200, 200, 200) ' Light grey background

    ' Auto-fit all columns in the used range of the active sheet
    ActiveSheet.UsedRange.Columns.AutoFit

    ' Add borders to the data range (assuming data starts from row 2)
    Dim DataRange As Range
    Set DataRange = Range("A2").CurrentRegion
    DataRange.Borders.LineStyle = xlContinuous

End Sub