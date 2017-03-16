using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Nexus_V1._0
{
    public partial class Hub : Form
    {
        public Hub()
        {
            InitializeComponent();
        }

        private void Hub_Load(object sender, EventArgs e)
        {
            // Buttons Begin
            List<string> Values = ChaosUnbound.ListTopics(0);

            List<Button> Buttons = new List<Button>();
            Buttons.Add(Btn1);
            Buttons.Add(Btn2);
            Buttons.Add(Btn3);
            Buttons.Add(Btn4);
            Buttons.Add(Btn5);
            Buttons.Add(Btn6);
            Buttons.Add(Btn7);
            Buttons.Add(Btn8);
            Buttons.Add(Btn9);
            Buttons.Add(Btn10);
            Buttons.Add(Btn11);
            Buttons.Add(Btn12);
            Buttons.Add(Btn13);
            Buttons.Add(Btn14);

            int CurrentButton = 0;
            foreach (var Val in Values)
            {
                Buttons[CurrentButton].Text = Val;
                CurrentButton++;
            }
            // Buttons End
            
            BtnBack.Enabled = false;

        }
    }
}
