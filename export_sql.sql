WbExport -type=sqlinsert 
         -file='heart_rate.sql' 
--         -file='table.csv'
         -table='heart_rate';

select  heart_rate.device_id, heart_rate.rri, heart_rate.tstamp from (
    select * from (
    select device_id, day, count(*) as notnullcount from
    (select device_id, trunc(tstamp) as day, rri, hr from heart_rate where rri is not null and tstamp >= date_trunc('day',getdate())-90
       and tstamp < date_trunc('day',getdate())-89 
    )
    group by device_id, day

  ) where notnullcount< 86400 order by notnullcount desc limit 10
) as topactivedevice,
heart_rate where topactivedevice.device_id=heart_rate.device_id and heart_rate.tstamp>=date_trunc('day',getdate())-90
 and heart_rate.tstamp < date_trunc('day',getdate())-89  limit 2000000
