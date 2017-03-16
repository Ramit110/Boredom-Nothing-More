using System.Collections.Generic;

namespace Nexus_V1._0
{
    /*
    Acronyms:
        TBR = To Be Returned
    */
    class ChaosUnbound
    {
        public class Main
        {
            public string Topics { get; set; }
            public string Calc { get; set; }
        }

        public static List<string> ListMainMenu()
        /*
            FirstVar: The Number Of The Firts Topic In The Retuned List

            [0]-[13] = Each Page
        */
        {
            List<string> TBR = new List<string>() { }; // TBR = To Be Returned
            
            // MUST BE IN ALPHABETICAL ORDER
            TBR.Add("Project Euler Experiments"); // 0

            return TBR;
        }

        public static List<Main> ListSubMenu(int FirstVar, int InitState)
        /*
            FirstVar: Class Above Dictates Which 'Topic' To Choose From
            InitStage: Corresponds To How Many Results To Skip Before Adding To The Table

            The reurned list will go in order from: [0]-[13] = Each Page
        */
        {
            List<Main> TBR = new List<Main>() { };
            List<string> MainMenu = ListMainMenu();
            


            return TBR;
        }
    }
}
