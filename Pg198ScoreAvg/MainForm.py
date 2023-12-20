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
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(120, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Score 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Plum
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 77)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(120, 37)
		self._label2.TabIndex = 1
		self._label2.Text = "Score 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Plum
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 128)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(120, 37)
		self._label3.TabIndex = 2
		self._label3.Text = "Score 3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Plum
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 187)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(120, 37)
		self._label4.TabIndex = 3
		self._label4.Text = "Avrage:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(138, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(234, 38)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(138, 74)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(234, 38)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(138, 128)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(234, 38)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Plum
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(138, 187)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(234, 37)
		self._label5.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 256)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(143, 38)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(161, 256)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 38)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(263, 256)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(109, 38)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Purple
		self.ClientSize = System.Drawing.Size(384, 306)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg198ScoreAvg"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		n = float(self._textBox1.Text)
		o = float(self._textBox2.Text)
		p = float(self._textBox3.Text)
		e = (n + o + p)/3
		self._label5.Text = str(round(e, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._textBox3.Clear()
		self._label5.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()