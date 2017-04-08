using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace Nexus_V1._0
{
    public partial class Hub : Form
    {
        public int PageNum = 0;

        public Hub()
        {
            InitializeComponent();
        }

        private void Hub_Load(object sender, EventArgs e)
        {
            // Buttons Begin

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

            ChaosUnbound Chaos = new ChaosUnbound();
            Buttons = Chaos.AssignMenu(Buttons, PageNum+1, "Main");
            if(Buttons[13].Enabled == false)
            {
                BtnForwards.Enabled = false;
            }
            Buttons = Chaos.AssignMenu(Buttons, PageNum, "Main");
            BtnBack.Enabled = false;

            // Buttons End
        }

        private void BtnBack_Click(object sender, EventArgs e)
        {

        }

        private void BtnForwards_Click(object sender, EventArgs e)
        {

        }
    }
}
