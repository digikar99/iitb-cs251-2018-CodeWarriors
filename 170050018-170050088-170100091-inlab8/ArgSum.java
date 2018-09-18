class ArgSum {
 public static void main(String[] args){
 	int sum=0;
 	for ( int i = 0; i < args.length; i++ ){
 		int result = Integer.parseInt(args[i]);
 		sum=sum+result;
 	}
 	System.out.println(args.length + "," + sum);
 	}
 }