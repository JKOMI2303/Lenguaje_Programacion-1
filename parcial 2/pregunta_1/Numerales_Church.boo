import System
import System.Runtime.CompilerServices


public callable Church(f as Church) as Church

[module]
internal static class ChurchNumeral:

	public static final ChurchZero as Church = { __ | return { x | return x } }

	public static final ChurchOne as Church = { f | return f }


	[Extension]
	public static def Add(m as Church, n as Church) as Church:
		return { f | return { x | return m(f)(n(f)(x)) } }

	[Extension]
	public static def Multiply(m as Church, n as Church) as Church:
		return { f | return m(n(f)) }


	public static def Main():
		c3 as Church = FromInt(3)
		c4 as Church = c3.Successor()
		c11 as Church = FromInt(11)
		c12 as Church = c11.Successor()
		sum as int = c3.Add(c4).ToInt()
		product as int = c3.Multiply(c4).ToInt()
		Console.WriteLine(sum)
		Console.WriteLine(product)

