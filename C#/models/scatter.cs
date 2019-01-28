using Imsl.Chart2D;
using System.Drawing;

public class SampleSimpleScatter : FrameChart {

    public SampleSimpleScatter() {
        Chart chart = this.Chart;
        AxisXY axis = new AxisXY(chart);

        double[] y = new double[] {8, 3, 5, 2, 9};
        Data data1 = new Data(axis, y);
        data1.DataType = Data.DATA_TYPE_MARKER;
        data1.MarkerType = Data.MARKER_TYPE_FILLED_SQUARE;
        data1.MarkerColor = Color.Blue;
    }

    public static void Main(string[] argv) {
        System.Windows.Forms.Application.Run(new SampleSimpleScatter());
    }
}
