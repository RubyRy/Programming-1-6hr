import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.SlateBlue
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Location = System.Drawing.Point(26, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(249, 159)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.SlateBlue
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox2.Location = System.Drawing.Point(321, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(249, 159)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Options"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.SlateBlue
		self._groupBox3.Controls.Add(self._textBox1)
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox3.Location = System.Drawing.Point(26, 174)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(249, 101)
		self._groupBox3.TabIndex = 1
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Membership Length"
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.SlateBlue
		self._groupBox4.Controls.Add(self._label5)
		self._groupBox4.Controls.Add(self._label4)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox4.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox4.Location = System.Drawing.Point(321, 174)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(249, 101)
		self._groupBox4.TabIndex = 1
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Membership Fees"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 25)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(237, 38)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Standered Adult"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 53)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(237, 38)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (12 && Under)"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 83)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(237, 38)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(6, 115)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(237, 38)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(6, 25)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(237, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(6, 67)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(237, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(6, 115)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(237, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(237, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the Number of Months:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(6, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(226, 26)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label2.Location = System.Drawing.Point(6, 34)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Monthly Fee:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(58, 63)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(48, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Total:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.GhostWhite
		self._label4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label4.Location = System.Drawing.Point(112, 34)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(131, 23)
		self._label4.TabIndex = 2
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.GhostWhite
		self._label5.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label5.Location = System.Drawing.Point(112, 63)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(131, 23)
		self._label5.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(26, 281)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(177, 38)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(209, 281)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(164, 38)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(379, 281)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(191, 38)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(593, 325)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg250MembershipFee"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		BaseFee = 0.0
		Discount = 0.0
		Total = 0.0
		Months = int(self._textBox1.Text)
		if Months < 1 or Months > 24:
			MessageBox.Show("Input invaild")
		
		if self._radioButton1.Checked == True:
			BaseFee = 40
		elif self._radioButton2.Checked == True:
			BaseFee = 20
		elif self._radioButton3.Checked == True:
			BaseFee = 25
		elif self._radioButton4.Checked == True:
			BaseFee = 30
		
		if self._checkBox1.Checked == True:
			BaseFee += 10
		if self._checkBox2.Checked == True:
			BaseFee += 30
		if self._checkBox3.Checked == True:
			BaseFee += 50
		
		if Months <= 3:
			Discount = 0.0
		elif Months >= 4 and Months <= 6:
			Discount = BaseFee * 0.05
		elif Months >= 7 and Months <= 9:
			Discount = BaseFee * 0.08
		elif Months >= 10:
			Discount = BaseFee * 0.1
			
		BaseFee -= Discount
		Total = BaseFee * Months 
		self._label4.Text = str(round(BaseFee, 2))
		self._label5.Text = str(round(Total, 2))

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = True
		self._checkBox1.Checked = False
		self._checkBox2.Checked = False
		self._checkBox3.Checked = False
		self._textBox1.Clear()
		self._label4.Text = " "
		self._label5.Text = " "