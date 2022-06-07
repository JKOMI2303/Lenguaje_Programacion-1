
public class pregunta_1_parte_b {
	
	
	public static int modulo(int a,int b,int c) {
		if(b==0) {
			int x=1;
			return x;
		}else if(b>0){
			int z=(int) Math.pow(a, b-1);
			int x=( ((a%c)*(z%c)) % c );
			return x;					
		}else {
			return -1;
		}
		
	}
	public static int[][] MultMatriz(int[][] A,int[][] B){
		int rowA=A.length;
		int colA=A[0].length;
		int colB=B[0].length;
		int result_matriz [][]=new int[rowA][colB];
		for(int i=0;i<rowA;i++) {
			for(int j=0;j<colB;j++) {
				for(int k=0;k<colA;k++) {
					result_matriz[i][j]+=A[i][k]*B[k][j];
				}
			}
		}
		
		return result_matriz;
		
	}

	public static void main(String[] args) {
		System.out.println(modulo(5,0,4));
		int[][] A= {{1,2,3},{1,1,1},{0,1,-1}};
		int[][] B= {{1},{2},{1}};
		int[][] C=MultMatriz(A,B);
		
		for (int x=0; x < C.length; x++) {
			  System.out.print("|");
			  for (int y=0; y < C[x].length; y++) {
			    System.out.print (C[x][y]);
			    if (y!=C[x].length-1) System.out.print("\t");
			  }
			  System.out.println("|");
			}
		
	}

}
