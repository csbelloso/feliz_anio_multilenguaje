VERSION 5.00
Object = "{6B7E6392-850A-101B-AFC0-4210102A8DA7}#1.3#0"; "COMCTL32.OCX"
Begin VB.Form Form1 
   Caption         =   "Cerrar 2024 - Abrir 2025 by CSB "
   ClientHeight    =   2490
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   4680
   LinkTopic       =   "Form1"
   ScaleHeight     =   2490
   ScaleWidth      =   4680
   StartUpPosition =   2  'CenterScreen
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   10
      Left            =   240
      Top             =   1320
   End
   Begin ComctlLib.ProgressBar ProgressBar1 
      DragMode        =   1  'Automatic
      Height          =   495
      Left            =   120
      TabIndex        =   4
      Top             =   1800
      Visible         =   0   'False
      Width           =   4455
      _ExtentX        =   7858
      _ExtentY        =   873
      _Version        =   327682
      Appearance      =   0
      Max             =   366
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Empezar Proceso"
      Height          =   375
      Left            =   2040
      TabIndex        =   3
      Top             =   600
      Width           =   2175
   End
   Begin VB.CheckBox Check2 
      Caption         =   "Cerrar 2024"
      Height          =   255
      Left            =   240
      TabIndex        =   2
      Top             =   840
      Width           =   3255
   End
   Begin VB.CheckBox Check1 
      Caption         =   "Recopilar 2024"
      Height          =   255
      Left            =   240
      TabIndex        =   0
      Top             =   480
      Width           =   3255
   End
   Begin VB.Frame Frame1 
      Caption         =   "2024"
      Height          =   975
      Left            =   120
      TabIndex        =   1
      Top             =   240
      Width           =   4455
   End
   Begin VB.Image Image1 
      Height          =   4200
      Left            =   120
      Picture         =   "Form1.frx":0000
      Stretch         =   -1  'True
      Top             =   2400
      Visible         =   0   'False
      Width           =   4440
   End
   Begin VB.Label Label1 
      Alignment       =   1  'Right Justify
      Caption         =   "Recopilado 0 de 366 dias"
      Height          =   255
      Left            =   1440
      TabIndex        =   5
      Top             =   1440
      Visible         =   0   'False
      Width           =   3015
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Label1.Visible = True
ProgressBar1.Visible = True
Timer1.Enabled = True
ProgressBar1.Min = 0
ProgressBar1.Max = 366
ProgressBar1.Value = 0
End Sub


Private Sub Timer1_Timer()
Dim respuesta As Integer
If ProgressBar1 < 366 Then
ProgressBar1.Value = ProgressBar1.Value + 1
Label1.Caption = "Recopilando " & ProgressBar1 & " de 366 dias"

Else
Timer1.Enabled = False
respuesta = MsgBox("Año 2024 Cerrado" & vbCrLf & "Balance POSITIVO", vbOKOnly, "2024 Cerrado y OK")
End If
If respuesta = 1 Then
Form1.Height = 7080
Image1.Visible = True
End If

End Sub
