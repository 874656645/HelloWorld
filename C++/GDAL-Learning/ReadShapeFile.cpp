#include<iostream>
#include<gdal.h>

#pragma comment(lib, "gdal_i.lib")

using namespace std;

int main(int argc, char const *argv[])
{
    GDALAllRegister();
    GDALDatasetH poDS;
    // CPLSetConfigOption("SHAPE_ENCODING","");    //解决中文乱码问题
    
    //读取shp文件
    poDS = (GDALDatasetH*) GDALOpenEx("D:/GitHub/HelloWorld/C++/GDAL-Learning/data/pro_9000/pro_102100_9000.shp", GDAL_OF_VECTOR, NULL, NULL, NULL );
    
    if( poDS == NULL )
    {
        printf( "Open failed.\n%s" );
        return 0;
    }

    OGRLayerH poLayer = GDALDatasetGetLayer(poDS, 0); //读取层
    OGRFeatureH poFeature;

    GDALDatasetResetReading(poDS);
    int i=0;
    // while( (poFeature = GDALDatasetGetNextFeature(poDS, poLayer)) != NULL )
    // {
    //     if(poFeature->GetFieldAsDouble("AREA")<1) continue; //去掉面积过小的polygon
    //     i = i++;
    //     cout << i << "\t";
    //     OGRFeatureDefnH *poFDefn = poLayer->GetLayerDefn();
    //     int iField;
    //     int n = poFDefn->GetFieldCount(); //获得字段的数目，不包括前两个字段（FID,Shape);
    //     for( iField = 0; iField <n; iField++ )
    //     {
    //         //输出每个字段的值
    //         cout << poFeature->GetFieldAsString(iField) << "\t";
    //     }
    //     cout<<endl;
    //     DestroyFeature( poFeature );
    // }
    GDALClose( poDS );
    system("pause");
    return 0;
}
