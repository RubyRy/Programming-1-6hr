import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(1, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(302, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of Calories:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(1, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(302, 35)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter the number of Grams:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(1, 119)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(302, 52)
		self._label3.TabIndex = 2
		self._label3.Text = "Precentage of Calories that come from Fat:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 190)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 45)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculator"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(156, 190)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 45)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(295, 190)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(122, 45)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(309, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(108, 35)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(309, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(108, 35)
		self._textBox2.TabIndex = 7
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(309, 119)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(108, 52)
		self._label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RoyalBlue
		self.ClientSize = System.Drawing.Size(429, 244)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg268FatCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Grams = float(self._textBox2.Text)
		C = float(self._textBox1.Text)
		P = (Grams * 9)/C * 100
		self._label4.Text = str(round(P, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._label4.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()