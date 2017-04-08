using System.Collections.Generic;
using System.Windows.Forms;

namespace Nexus_V1._0
{
    /*
    Acronyms:
        TBR = To Be Returned
    */
    public class ChaosUnbound
    {
        public List<Button> AssignMenu(List<Button> Buttons, int Page, string Menu)
        {
            Dictionary<string, List<string>> Menus = new Dictionary<string, List<string>>();

            // Clear Menu
            Buttons = BtnArrFill(Buttons, 0, "");

            // Main Menu ONLY HARD CODED MENU !!!
            List<string> MainMenu = new List<string>();
            MainMenu.Add("Math Stuff");
            MainMenu.Add("Project Euler(C#)");
            Menus.Add("Main", MainMenu);

            int EndPoint = (Page + 14);

            while ((EndPoint >= (Page - 14)) && (EndPoint >= Menus[Menu].Count))
            {
                EndPoint--;
            }

            for (int x = Page; x <= EndPoint; x++)
            {
                if (Menus.ContainsKey(Menu))
                {
                    Buttons[x].Text = Menus[Menu][x];
                    Buttons[x].Enabled = true;
                }
            }

            foreach (Button Btn in Buttons)
            {
                if (Btn.Text == "")
                {
                    Btn.Enabled = false;
                }
            }
            return Buttons;
        }

        private List<Button> BtnArrFill(List<Button> Buttons, int Conditions, string Rename)
        {
            foreach (Button Btn in Buttons)
            {
                if ((Btn.Text == "") || (Conditions == 0))
                {
                    Btn.Text = Rename;
                }
            }
            return Buttons;
        }
    }
}