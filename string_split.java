int intc=0;
        int doublec=0;
        int stringc=0;
        boolean iflag=true,dflag=true;
       
        String s2[]=sentence.split(" ");
        for(int i=0;i<s2.length;i++)
        {
          try
          {
            Integer d= Integer.parseInt(s2[i]);
          }  
          catch(NumberFormatException ex1)
          {
              iflag=false;
          }
          
          if(iflag==false)
          {
              try{
                  Double dd=Double.parseDouble(s2[i]);
              }
              catch(NumberFormatException ex2)
              {
                  dflag=false;
              }
          }
          
          if(iflag)
          {
              intc=intc+1;
          }
          if(dflag==true && iflag==false)
          {
              doublec+=1;
          }
          if(dflag==false)
          {
              stringc=stringc+1;
          }
          
          iflag=true;
          dflag=true;
          
          
          
        }
        System.out.println("string "+stringc);
        System.out.println("integer "+intc);
        System.out.println("double "+doublec);