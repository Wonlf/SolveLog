using System;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
	// Token: 0x02000003 RID: 3
	public class Form1 : Form
	{
		// Token: 0x06000005 RID: 5 RVA: 0x000020A6 File Offset: 0x000002A6
		protected override void Dispose(bool disposing)
		{
			if (disposing && this.components != null)
			{
				this.components.Dispose();
			}
			base.Dispose(disposing);
		}

		// Token: 0x06000006 RID: 6 RVA: 0x000020C8 File Offset: 0x000002C8
		private void InitializeComponent()
		{
			this.textBox1 = new TextBox();
			this.button1 = new Button();
			this.textBox2 = new TextBox();
			this.button2 = new Button();
			this.label1 = new Label();
			base.SuspendLayout();
			this.textBox1.Location = new Point(12, 12);
			this.textBox1.Name = "textBox1";
			this.textBox1.Size = new Size(268, 20);
			this.textBox1.TabIndex = 0;
			this.textBox1.Text = "HMX0101";
			this.button1.Location = new Point(12, 64);
			this.button1.Name = "button1";
			this.button1.Size = new Size(75, 23);
			this.button1.TabIndex = 1;
			this.button1.Text = "Check";
			this.button1.UseVisualStyleBackColor = true;
			this.button1.Click += this.button1_Click;
			this.textBox2.Font = new Font("Microsoft Sans Serif", 8.25f, FontStyle.Bold, GraphicsUnit.Point, 0);
			this.textBox2.Location = new Point(12, 38);
			this.textBox2.Name = "textBox2";
			this.textBox2.Size = new Size(268, 20);
			this.textBox2.TabIndex = 2;
			this.button2.Location = new Point(93, 64);
			this.button2.Name = "button2";
			this.button2.Size = new Size(75, 23);
			this.button2.TabIndex = 3;
			this.button2.Text = "Close";
			this.button2.UseVisualStyleBackColor = true;
			this.button2.Click += this.button2_Click;
			this.label1.Enabled = false;
			this.label1.Location = new Point(174, 69);
			this.label1.Name = "label1";
			this.label1.Size = new Size(100, 23);
			this.label1.TabIndex = 4;
			this.label1.Text = "...::: HMX0101 :::...";
			this.label1.TextAlign = ContentAlignment.TopCenter;
			base.AutoScaleDimensions = new SizeF(6f, 13f);
			base.AutoScaleMode = AutoScaleMode.Font;
			base.ClientSize = new Size(292, 94);
			base.Controls.Add(this.label1);
			base.Controls.Add(this.button2);
			base.Controls.Add(this.textBox2);
			base.Controls.Add(this.button1);
			base.Controls.Add(this.textBox1);
			base.FormBorderStyle = FormBorderStyle.FixedDialog;
			base.MaximizeBox = false;
			base.Name = "Form1";
			this.Text = "Spare Time - Coded by: HMX0101";
			base.Load += this.Form1_Load;
			base.ResumeLayout(false);
			base.PerformLayout();
		}

		// Token: 0x06000007 RID: 7 RVA: 0x000023F0 File Offset: 0x000005F0
		public Form1()
		{
			this.InitializeComponent();
		}

		// Token: 0x06000008 RID: 8 RVA: 0x00002418 File Offset: 0x00000618
		public static byte[] dfgsf(string str)
		{
			ASCIIEncoding asciiencoding = new ASCIIEncoding();
			return asciiencoding.GetBytes(str);
		}

		// Token: 0x06000009 RID: 9 RVA: 0x00002434 File Offset: 0x00000634
		private bool vxzzz(uint[] rwerqw, uint[] kgtsdfs, uint pgdsfa, uint fsfsdf)
		{
			pgdsfa ^= fsfsdf;
			uint num = pgdsfa % 57U - 1U;
			uint num2 = rwerqw[0];
			uint num3 = rwerqw[1];
			uint num4 = num;
			uint num5 = pgdsfa << (int)((byte)(97U ^ num + 68U));
			if (num == 0U)
			{
				return false;
			}
			while (num-- > 0U)
			{
				uint num6 = num4 / 16U;
				uint num7 = num2 << (int)((byte)(num4 / 8U));
				uint num8 = num2 >> (int)(3 + (byte)num6);
				uint num9 = num4 / 4U + 3U;
				uint num10 = num9;
				num9 = kgtsdfs[(int)((UIntPtr)((num5 >> (int)((byte)num9)) % 4U))];
				uint num11 = num5 + num9;
				num3 -= ((num7 ^ num8) + num2 ^ num11) - num;
				num5 -= pgdsfa;
				num3 -= num;
				num7 = num3 << (int)((byte)(num10 + 1U) ^ 8);
				num8 = num3 >> (int)((byte)(num4 / 2U - num10 + 23U) ^ 25);
				if (num == num4)
				{
					num3 ^= num;
				}
				if (num == num4 / 2U + (num10 ^ 27U))
				{
					num10 = (num7 ^ num8) + (num3 ^ num);
				}
				else
				{
					num10 = (num7 ^ num8) + num3;
				}
				num2 -= (num10 ^ num5 + kgtsdfs[(int)((UIntPtr)(num5 & 3U))]);
			}
			rwerqw[0] = (num2 ^ 4U);
			rwerqw[1] = (num3 ^ 7U);
			rwerqw[2] = (rwerqw[1] ^ (uint)((byte)((num4 + 1U) / 3U - 4U)));
			rwerqw[3] = (rwerqw[0] ^ (uint)((byte)(num4 - 21U + 1U ^ 8U)));
			rwerqw[0] = (rwerqw[0] ^ kgtsdfs[4]);
			rwerqw[1] = (rwerqw[1] ^ kgtsdfs[5]);
			return true;
		}

		// Token: 0x0600000A RID: 10
		private void button1_Click(object sender, EventArgs e)
		{
			string text = "";
			string text2 = "";
			string text3 = "";
			ytrewq ytrewq = new ytrewq();
			if (this.textBox1.Text.Length >= 5 && this.textBox1.Text.Length <= 27 && this.textBox2.Text.Length == 26 && this.textBox2.Text[8] == '-' && this.textBox2.Text[17] == '-')
			{
				for (int i = 0; i < 8; i++)
				{
					text += this.textBox2.Text[i].ToString();
				}
				uint num = Convert.ToUInt32(text, 16);
				for (int j = 9; j < 17; j++)
				{
					text2 += this.textBox2.Text[j].ToString();
				}
				uint num2 = Convert.ToUInt32(text2, 16);
				for (int k = 18; k < 26; k++)
				{
					text3 += this.textBox2.Text[k].ToString();
				}
				for (uint l = 0U; l <= 4294967295U; l += 1U)
				{
					uint num3 = l;
					uint num4 = ytrewq.qwerty(Form1.dfgsf(this.textBox1.Text));
					uint hashCode = (uint)this.textBox1.Text.GetHashCode();
					num3 ^= hashCode;
					this.yreee[0] = num;
					this.yreee[1] = num2;
					this.yreee[2] = num;
					this.yreee[3] = num2;
					if (this.vxzzz(this.yreee, this.ewrrr, 2415796773U, num3) && this.yreee[2] == hashCode && this.yreee[3] == num4)
					{
						MessageBox.Show("Congratulations, mate!", "Fine!", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
						return;
					}
				}
			}
		}

		// Token: 0x0600000B RID: 11 RVA: 0x00002764 File Offset: 0x00000964
		private void button2_Click(object sender, EventArgs e)
		{
			Application.Exit();
		}

		// Token: 0x0600000C RID: 12 RVA: 0x0000276C File Offset: 0x0000096C
		private void Form1_Load(object sender, EventArgs e)
		{
			this.ewrrr[0] = 1082200817U;
			this.ewrrr[1] = 440077137U;
			this.ewrrr[2] = 693619197U;
			this.ewrrr[3] = 456293661U;
			this.ewrrr[4] = 2743929585U;
			this.ewrrr[5] = 718661953U;
		}

		// Token: 0x04000003 RID: 3
		private IContainer components;

		// Token: 0x04000004 RID: 4
		private TextBox textBox1;

		// Token: 0x04000005 RID: 5
		private Button button1;

		// Token: 0x04000006 RID: 6
		private TextBox textBox2;

		// Token: 0x04000007 RID: 7
		private Button button2;

		// Token: 0x04000008 RID: 8
		private Label label1;

		// Token: 0x04000009 RID: 9
		private uint[] ewrrr = new uint[6];

		// Token: 0x0400000A RID: 10
		private uint[] yreee = new uint[4];
	}
}
